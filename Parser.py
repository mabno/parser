from funciones import simbolosDirectrices, cadenizacion
from gramaticas import gramatica
from lexer import lexer


SD = {
  'Program': [{'func', 'si', 'repetir', 'mostrar', 'id', 'leer'}],
  'ListaSentencias': [{'id', 'si', 'leer', 'repetir', 'mostrar', 'func'}],
  "ListaSentencias'": [{'#', 'sino', 'finsi', 'finfunc', 'hasta'}, {';'}],
  'Sentencia': [{'si'}, {'func'}, {'id'}, {'leer'}, {'mostrar'}, {'repetir'}],
  'SentenciaSi': [{'si'}],
  "SentenciaSi'": [{'sino'}, {'finsi'}],
  'SentenciaFun': [{'func'}],
  'SentenciaAsig': [{'id'}],
  'SentenciaLeer': [{'leer'}],
  'SentenciaMostrar': [{'mostrar'}],
  'SentenciaRepetir': [{'repetir'}],
  'Proc': [{'id'}],
  'ListaPar': [{'id'}],
  "ListaPar'": [{')'}, {';'}],
  'Expresion': [{'id', '(', 'num'}],
  "Expresion'": [set(), {'oprel'}],
  'Expresion2': [{'id', '(', 'num'}],
  "Expresion2'": [{'oprel', 'pyc', 'finfunc', 'hasta', ')', '#', 'sino', 'entonces', 'finsi'}, {'opsuma'}],
  'Termino': [{'num', 'id', '('}],
  "Termino'": ['opsuma', 'oprel', 'pyc', 'finfunc', 'hasta', ')', '#', 'sino', 'entonces', 'finsi', {'opmult'}],
  'Factor': [{'('}, {'id'}, {'num'}]}


# Analizador sintáctico descendente predictivo
# Algoritmo sacado de los apuntes de la cátedra
def PeterFuckingParser(lista, gramatica):
  SimbolosDirectrices = SD
  # Variable capaz de detener el procedimiento
  error = False
  # Índice del puntero
  t = 0
  # Función recursiva spiderman: agarra un no terminal N -> α0 | α1 | ... | αk
  def spiderman(noTerminal):
    nonlocal error
    nonlocal t
    error = False
    # Para cada derivación αi del no terminal
    for i, derivacion in enumerate(gramatica['P'][noTerminal]):
      # Si el elemento al que apunta el puntero pertenece a SD(N -> αi)
      if lista[t] in SimbolosDirectrices[noTerminal][i]:
        # Para cada símbolo xj de αi
        for simbolo in derivacion:
          # Si el símbolo xj es un terminal
          if simbolo in gramatica['T']:
            # Si el puntero apunta al terminal xj
            if lista[t] == cadenizacion(simbolo):
              # Avanza el puntero en la cadena
              t += 1
            # Si el terminal xj no es apuntado
            else:
              # Tenemos un problema, señor
              error = True
              break
          # Si el símbolo xj es un no terminal
          elif simbolo in gramatica['N']:
            # Llamada recursiva a spiderman con el no terminal xj para que siga buscando al elemento apuntado
            spiderman(simbolo)
            # El error debe ser pagado
            if error:
              break
  # El hombre araña empieza a buscar desde el símbolo distinguido
  spiderman(gramatica['S'])
  # GOOD ENDING
  if not error and lista[t] == '#':
    print('PETER PARSER: Cadena aceptada')
  # BAD ENDING
  else:
    print('PETER PARSER: Cadena rechazada. No se puede derivar en el terminal "' + str(lista[t]) + '" de la posición ' + str(t) + '.')


# Pruebas

# Cadena de texto de entrada
cadena = 'si vgAuxi==7, entonces vgAuxi igual 1, sino leer libro. FinSi.'
# Lista de tokens devuelta por Hannibal Lexer
lista = [token[1] for token in lexer(cadena)]
print('Cadena de tokens: ' + str(lista))
PeterFuckingParser(lista, gramatica)

# Cadena de texto de entrada
cadena = 'función y(x): y equal (x * 2) + 3. Finfunción;\nz iqual y'
# Lista de tokens devuelta por Hannibal Lexer
lista = [token[1] for token in lexer(cadena)]
print('Cadena de tokens: ' + str(lista))
PeterFuckingParser(lista, gramatica)

# Cadena de texto de entrada
cadena = 'si vgAuxi igual 7, entonces vgAuxi == 1, sino mostrar demostración. FinSi.'
# Lista de tokens devuelta por Hannibal Lexer
lista = [token[1] for token in lexer(cadena)]
print('Cadena de tokens: ' + str(lista))
PeterFuckingParser(lista, gramatica)

# Cadena de texto de entrada
cadena = 'func y(x): leer y finfuncion; Repetir x equal x + 1 hasta x>=y.'
# Lista de tokens devuelta por Hannibal Lexer
lista = [token[1] for token in lexer(cadena)]
print('Cadena de tokens: ' + str(lista))
PeterFuckingParser(lista, gramatica)
