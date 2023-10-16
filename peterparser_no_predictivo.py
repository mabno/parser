"""
  Implementación procedural de analizadores sintácticos descendentes con retroceso
  NO PREDICTIVO
"""

# Terminales
abre_parentesis = '('
cierra_parentesis = ')'
a = 'a'
c = 'c'
VT = [a, c, abre_parentesis, cierra_parentesis]

# No terminales
S = 'S'
B = 'B'
VN = [S, B]

# Producciones
P = {
  S: [[abre_parentesis, B, cierra_parentesis], [a]],
  B: [c]
}

# Cadena de entrada
cadena = '(c)'

# Glorioso POO
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

def main(w):
  # Definimos las variables globales transversales a los procedimientos
  error = Error()
  puntero = Puntero()

  # Comprueba que el puntero ya este "apuntando" al fin de la cadena
  def fin_de_cadena(w):
    return puntero.obtener() == len(w)

  def PNI(VN):
    # Obtiene en que puede derivar VN
    producciones = P.get(VN)
    k = len(producciones)

    j = 0
    
    # Mientras no haya error y no se hayan probado todas las producciones
    while True:
      error.desactivar()
      procesar(producciones[j])
      j = j + 1

      if not(error.obtener() and j < k):
        break


  def procesar(produccion):
    for j in range(0, len(produccion)):
      t = puntero.obtener()
      # Obtengo el simbolo de la produccion en la posicion j
      xj = produccion[j]
      # Si es un terminal
      if xj in VT:
       
        if t < len(w) and w[t] == xj:  # t < len(w) para evitar IndexError
          puntero.avanzar()
        else:
          error.activar()
          break
      # Si es un no terminal
      if xj in VN:
        
        PNI(xj)
        if error.obtener():
          break
      


  PNI(S)
  if not error.obtener() and fin_de_cadena(w):
    print('Cadena aceptada')
  else:
    print('Cadena rechazada')
  

main(cadena)