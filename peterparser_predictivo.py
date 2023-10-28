"""
  Implementación procedural de analizadores sintácticos descendentes predictivo.
  Esta version es predictiva ya que se tienen los simbolos directrices de las producciones de la gramatica
"""

from Parser import simbolosDirectrices, cadenizacion, primeros, siguientes, λ
from automatas import sino, si, entonces, func, finfunc, finsi, repetir, hasta, equal, leer, mostrar, parentesisI, parentesisD, id, num, oprel, opsuma, opmult, pyc
from gramaticas import gramatica, gramaticaSTR


# Cadena de entrada
cadena = [id, equal, num, opmult, parentesisI, num, opsuma, num, parentesisD]

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
  simbolosDirectricesGramatica = simbolosDirectrices(gramatica)
  print(simbolosDirectricesGramatica)

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

        if t < len(cadena) and cadenizacion(cadena[t]) == cadenizacion(xj):  # t < len(w) para evitar IndexError
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
    print('Cadena aceptada')
  else:
    print('Cadena rechazada')


main(cadena, gramatica)

'''
      __                                                      
     /  l                                                     
   .'   :               __.....__..._  ____                   
  /  /   \          _.-"        "-.  ""    "-.                
 (`-: .---:    .--.'          _....J.         "-.             
  """y     \,.'    \  __..--""       `+""--.     `.           
    :     .'/    .-"""-. _.            `.   "-.    `._.._     
    ;  _.'.'  .-j       `.               \     "-.   "-._`.   
    :    / .-" :          \  `-.          `-      "-.      \  
     ;  /.'    ;          :;               ."        \      `,
     :_:/      ::\        ;:     (        /   .-"   .')      ;
       ;-"      ; "-.    /  ;           .^. .'    .' /    .-" 
      /     .-  :    `. '.  : .- / __.-j.'.'   .-"  /.---'    
     /  /      `,\.  .'   "":'  /-"   .'       \__.'          
    :  :         ,\""       ; .'    .'      .-""              
   _J  ;         ; `.      /.'    _/    \.-"                  
  /  "-:        /"--.b-..-'     .'       ;                    
 /     /  ""-..'            .--'.-'/  ,  :                    
:`.   :     / : bug         `-i" ,',_:  _ \                   
:  \  '._  :__;             .'.-"; ; ; j `.l                  
 \  \          "-._         `"  :_/ :_/                       
  `.;\             "-._                                       
    :_"-._             "-.                                    
      `.  l "-.     )     `.                                  
        ""^--""^-. :        \                                 
                  ";         \                                
                  :           `._                             
                  ; /    \ `._   ""---.                       
                 / /   _      `.--.__.'                       
                : :   / ;  :".  \                             
                ; ;  :  :  ;  `. `.                           
               /  ;  :   ; :    `. `.                         
              /  /:  ;   :  ;     "-'                         
             :_.' ;  ;    ; :                                 
                 /  /     :_l                                 
                 `-'
'''
