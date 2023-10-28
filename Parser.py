from automatas import sino, si, entonces, func, finfunc, finsi, repetir, hasta, equal, leer, mostrar, parentesisI, parentesisD, id, num, oprel, opsuma, opmult, pyc
from gramaticas import gramatica, gramaticaSTR


# Conjunto vacío
Ø = set([])
# cadenizacion vacía (lamdita)
λ = ""


# Función auxiliar que devuelve la cadenizacion asociada a un terminal, o un no terminal
def cadenizacion(simbolo):
  # Si el símbolo es una cadenizacion, devuelve la misma
  if isinstance(simbolo, str):
    return simbolo
  else:
    # Si es un terminal en su forma canónica, le asigna su valor clave
    return simbolo[5]


# Función que devuelve un diccionario con los primeros de cada símbolo
# Versión del libro "compiling an engineer"
def primeros(gramatica):
  # Diccionario con los primeros (conjunto) de cada símbolo (claves)
  primeros = {λ: Ø}
  primerosAux = {λ: Ø}
  # Para cada terminal, se agrega al mismo terminal al conjunto de primeros
  for terminal in gramatica['T']:
    primeros[cadenizacion(terminal)] = {cadenizacion(terminal)}
  # Para cada no terminal, se crea un conjunto vacío de primeros
  for noTerminal in gramatica['N']:
    primeros[noTerminal] = Ø
  # Mientras hayan cambios en primeros
  while primeros != primerosAux:
    primerosAux = primeros.copy()
    # Para cada producción (A -> β | ...) de la gramática
    for produccion in gramatica['P']:
      # Para cada derivación β0β1...βk de la producción
      for derivacion in gramatica['P'][produccion]:
        k = len(derivacion) - 1
        # primeros(A) = primeros(A) U (primeros(β0) - {λ})
        primeros[produccion] = primeros[produccion].union(
            primeros[cadenizacion(derivacion[0])].difference({λ}))
        i = 0
        while λ in primeros[cadenizacion(derivacion[i])] and i < k:
          # primeros(A) = primeros(A) U (primeros(β(i + 1)) - {λ})
          primeros[produccion] = primeros[produccion].union(
              primeros[cadenizacion(derivacion[i + 1])].difference({λ}))
          i += 1
        if i == k and λ in primeros[cadenizacion(derivacion[k])]:
          # primeros(A) = primeros(A) U {λ}
          primeros[produccion] = primeros[produccion].union({λ})
  return primeros


# Función que devuelve un diccionario con los siguientes de cada no terminal
# Versión del libro "compiling an engineer"
def siguientes(gramatica):
  # Diccionario con los sigiuentes (conjunto) de cada no terminal (claves)
  siguientes = {λ: Ø}
  siguientesAux = {λ: Ø}
  # Para cada no terminal, se crea una lista vacía de siguientes
  for noTerminal in gramatica['N']:
    siguientes[noTerminal] = Ø
  # Se agrega el símbolo de "fin de cadenizacion" a los siguientes del símbolo distinguido
  siguientes[gramatica['S']] = ['#']
  # Para cada terminal, se crea un conjunto vacío de siguientes (no está en el libro, pero el código no funciona sin esto)
  for terminal in gramatica['T']:
    siguientes[cadenizacion(terminal)] = Ø
  # Mientras hayan cambios en siguientes
  while siguientes != siguientesAux:
    siguientesAux = siguientes.copy()
    # Para cada producción (A -> β | ...) de la gramática
    for produccion in gramatica['P']:
      # Para cada derivación β0β1...βk de la producción
      for derivacion in gramatica['P'][produccion]:
        k = len(derivacion) - 1
        # siguientes(βk) = siguientes(βk) U siguientes(A)
        siguientes[cadenizacion(derivacion[k])] = siguientes[cadenizacion(derivacion[k])].union(
            siguientes[produccion])
        trailer = siguientes[produccion].copy()
        for i in range(k, 0, -1):
          if λ in siguientes[cadenizacion(derivacion[i])]:
            # siguientes(β(i-1)) = siguientes(β(i-1)) U (primeros(βi) - {λ}) U trailer
            siguientes[cadenizacion(derivacion[i - 1])] = (siguientes[cadenizacion(derivacion[i - 1])].union(
                primeros(gramatica)[cadenizacion(derivacion[i])].difference({λ}))).union(trailer)
          else:
            # siguientes(β(i-1)) = siguientes(β(i-1)) U primeros(βi)
            siguientes[cadenizacion(derivacion[i - 1])] = siguientes[cadenizacion(derivacion[i - 1])].union(primeros(gramatica)[cadenizacion(derivacion[i])])
            trailer = Ø
  return siguientes


# Función que determina si un no terminal es anulable
def anulable(noTerminal, gramatica):
  # α es anulable si y solo si λ ∈ primeros(α)
  return λ in primeros(gramatica)[noTerminal]


# Función que calcula los símbolos directrices de cada producción de una gramática
def simbolosDirectrices(gramatica):
  # Diccionario con los símbolos directrices (conjunto) de cada producción (clave) para cada derivación (elemento de una lista)
  simbolosDirectrices = {}
  # Para cada producción (A -> β0γ | β1δ | ...) de la gramática, con βi ∈ (T U N)
  for produccion in gramatica['P']:
    simbolosDirectrices[produccion] = Ø
    # Para cada derivación βiα de la producción
    for derivacion in gramatica['P'][produccion]:
      βi = cadenizacion(derivacion[0])
      # Si βi no es anulable, SD(producción) = primeros(βi)
      simbolosDirectrices[produccion] = (simbolosDirectrices[produccion]).union(primeros(gramatica)[βi])
      # Si βi es anulable, SD(producción) = primeros(βi) U siguientes(βi)
      if anulable(βi, gramatica):
        simbolosDirectrices[produccion] = (simbolosDirectrices[produccion]).union(siguientes(gramatica)[βi])
  return simbolosDirectrices


# Función que verifica si una gramática es LL(1)
def esLL1(gramatica):
  simbolos = simbolosDirectrices(gramatica)
  # Para cada producción (A -> β0γ | ... | βnδ) de la gramática, con βi ∈ (T U N)
  for produccion in simbolos:
    i = 0
    n = len(simbolos[produccion]) - 1
    while i < n:
      SDβi = list(simbolos[produccion])[i]
      for j in [k for k in range(i + 1, n + 1) if k != i]:
        SDβj = list(simbolos[produccion])[j]
        # Si SD(βi) ∩ SD(βj) != Ø
        if set(SDβi).intersection(set(SDβj)) != Ø:
          # La gramática no es LL(1)
          return False
      i += 1
  # Si llega acá, La gramática es LL(1)
  return True



print('Gramatica posta')
print('Primeros')
print(primeros(gramatica))
print('Siguientes')
print(siguientes(gramatica))
print('Simbolos directrices')
print(simbolosDirectrices(gramatica))
print('Es LL(1)')
print(esLL1(gramatica))
print()