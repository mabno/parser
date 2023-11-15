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


# Gloriosa programacion orientada a objetos
class Error:
  def __init__(self):
    self.__error = False

  def activar(self):
    self.__error = True

  def desactivar(self):
    self.__error = False

  def obtener(self):
    return self.__error


class Puntero:
  def __init__(self):
    self.__t = 0  # Puntero de la cadena de entrada

  def avanzar(self):
    self.__t = self.__t + 1

  def obtener(self):
    return self.__t


def main(cadena, gramatica):
  # Definimos los objetos globales transversales a los procedimientos
  error = Error()
  puntero = Puntero()
  simbolosDirectricesGramatica = SD

  # Comprueba que el puntero ya este "apuntando" al fin de la cadena
  def fin_de_cadena(cadena):
    return puntero.obtener() == len(cadena)

  def PNI(noTerminal):
    derivaciones = []
    # Obtiene en que puede derivar el no terminal
    derivaciones = gramatica['P'][noTerminal]

    error.desactivar()
    t = puntero.obtener()

    # Esta condicion fue agregada ya que en el caso
    # cadena = [int, id, pyc, id] teniamos la excepcion IndexError en simboloApuntado = w[t]
    if t >= len(cadena):
      error.activar()
      return

    simboloApuntado = cadena[t]
    # simbolosDirectricesGramatica.get(VN) devuelve los directrices de cada derivacion de VN
    # sd es el simbolo directriz
    # i es el indice de la derivacion a la cual pertenece el simbolo directriz
    # Ejemplo:
    # S -> (B) | a
    # simbolos directrices de S: ['(', 'a']
    # si simboloApuntado es '(' entonces i = 0 ya que '(' pertenece a la primera derivacion
    for i, sd in enumerate(simbolosDirectricesGramatica.keys()):
      if cadenizacion(simboloApuntado) == sd:
        derivacionQueFunciona = cadenizacion(derivaciones[i])
        procesar(derivacionQueFunciona)
        break

  def procesar(produccion):
    for j in range(0, len(produccion)):
      t = puntero.obtener()
      # Obtengo el simbolo de la produccion en la posicion j
      xj = produccion[j]
      # Si es un terminal
      if xj in gramatica['T']:

        # t < len(w) para evitar IndexError
        if t < len(cadena) and cadenizacion(cadena[t]) == cadenizacion(xj):
          puntero.avanzar()
        else:
          error.activar()
          break
      # Si es un no terminal
      if xj in gramatica['N']:

        PNI(xj)
        if error.obtener():
          break

  PNI(gramatica['S'])
  if not error.obtener() and fin_de_cadena(cadena):
    print('PETER PARSER: Cadena aceptada')
  else:
    print('PETER PARSER: Cadena rechazada. No se puede derivar en el terminal "' +
          str(lista[puntero.obtener()]) + '" de la posición ' + str(puntero.obtener()) + '.')


# Pruebas

# Cadena de texto de entrada
cadena = 'si vgAuxi==7, entonces vgAuxi igual 1, sino leer libro. FinSi.'
# Lista de tokens devuelta por Hannibal Lexer
lista = [token[1] for token in lexer(cadena)]
print('Cadena de tokens: ' + str(lista))
main(lista, gramatica)

# Cadena de texto de entrada
cadena = 'función y(x): y equal (x * 2) + 3. Finfunción;\nz iqual y'
# Lista de tokens devuelta por Hannibal Lexer
lista = [token[1] for token in lexer(cadena)]
print('Cadena de tokens: ' + str(lista))
main(lista, gramatica)

# Cadena de texto de entrada
cadena = 'si vgAuxi igual 7, entonces vgAuxi == 1, sino mostrar demostración. FinSi.'
# Lista de tokens devuelta por Hannibal Lexer
lista = [token[1] for token in lexer(cadena)]
print('Cadena de tokens: ' + str(lista))
main(lista, gramatica)

# Cadena de texto de entrada
cadena = 'func y(x): leer y finfuncion; Repetir x equal x + 1 hasta x>=y.'
# Lista de tokens devuelta por Hannibal Lexer
lista = [token[1] for token in lexer(cadena)]
print('Cadena de tokens: ' + str(lista))
main(lista, gramatica)
