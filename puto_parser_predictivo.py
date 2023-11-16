from gramaticas import gramaticaSTR
from lexer import lexer
from sd import SD


def principal(lista, gramatica):
  sd = SD
  error = False
  t = 0
  def P(noTerminal):
    nonlocal error 
    error = False
    for i, derivacion in enumerate(gramatica['P'][noTerminal]):
      def procesar(derivacion):
        nonlocal t
        nonlocal error
        for xj in derivacion:
          if xj in gramatica['T']:
            if lista[t] == xj:
              t += 1
            else:
              error = True
              break
          elif xj in gramatica['N']:
            P(xj)
            if error:
              break
      if lista[t] in sd[noTerminal]:
        procesar(derivacion)
  P(gramatica['S'])
  if not error and lista[t] == '#':
    print('Cadena aceptada')
  else:
    print('Cadena rechazada')


cadena = 'si vgAuxi==7, entonces vgAuxi igual 1, sino leer libro. FinSi.'
#print(lexer(cadena))
lista = [token[1] for token in lexer(cadena)]
#print(lista)
principal(lista, gramaticaSTR)
