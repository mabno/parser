# Conjunto vacío
Ø = set([])
# Cadena vacía (lamdita)
λ = ""


# Función que devuelve un diccionario con los primeros de cada símbolo
# Versión del libro "compiling an engineer"
def primeros(gramatica):
  # Diccionario con los primeros (conjunto) de cada símbolo (claves)
  primeros = {λ: Ø}
  primerosAux = {λ: Ø}
  # Para cada terminal, se agrega al mismo terminal al conjunto de primeros
  for terminal in gramatica['T']:
    primeros[terminal] = {terminal}
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
        primeros[produccion] = primeros[produccion].union(primeros[derivacion[0]].difference({λ}))
        i = 0
        while λ in primeros[derivacion[i]] and i < k:
          # primeros(A) = primeros(A) U (primeros(β(i + 1)) - {λ})
          primeros[produccion] = primeros[produccion].union(primeros[derivacion[i + 1]].difference({λ}))
          i += 1
        if i == k and λ in primeros[derivacion[k]]:
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
  # Se agrega el símbolo de "fin de cadena" a los siguientes del símbolo distinguido
  siguientes[gramatica['S']] = ['#']
  # Para cada terminal, se crea un conjunto vacío de siguientes (no está en el libro, pero el código no funciona sin esto)
  for terminal in gramatica['T']:
    siguientes[terminal] = Ø
  # Mientras hayan cambios en siguientes
  while siguientes != siguientesAux:
    siguientesAux = siguientes.copy()
    # Para cada producción (A -> β | ...) de la gramática
    for produccion in gramatica['P']:
      # Para cada derivación β0β1...βk de la producción
      for derivacion in gramatica['P'][produccion]:
        k = len(derivacion) - 1
        # siguientes(βk) = siguientes(βk) U siguientes(A)
        siguientes[derivacion[k]] = siguientes[derivacion[k]].union(siguientes[produccion])
        trailer = siguientes[produccion].copy()
        for i in range(k, 0, -1):
          if λ in siguientes[derivacion[i]]:
            # siguientes(β(i-1)) = siguientes(β(i-1)) U (primeros(βi) - {λ}) U trailer
            siguientes[derivacion[i - 1]] = (siguientes[derivacion[i - 1]].union(primeros(gramatica)[derivacion[i]].difference({λ}))).union(trailer)
          else:
            # siguientes(β(i-1)) = siguientes(β(i-1)) U primeros(βi)
            siguientes[derivacion[i - 1]] = siguientes[derivacion[i - 1]].union(primeros(gramatica)[derivacion[i]])
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
    simbolosDirectrices[produccion] = []
    # Para cada derivación βiα de la producción
    for derivacion in gramatica['P'][produccion]:
      βi = derivacion[0]
      # Si βi no es anulable, SD(producción) = primeros(βi)
      (simbolosDirectrices[produccion]).append(primeros(gramatica)[βi])
      # Si βi es anulable, SD(producción) = primeros(βi) U siguientes(βi)
      if anulable(βi, gramatica):
        (simbolosDirectrices[produccion]).append(siguientes(gramatica)[βi])
  return simbolosDirectrices
