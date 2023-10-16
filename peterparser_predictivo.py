"""
  Implementación procedural de analizadores sintácticos descendentes predictivo.
  Esta version es predictiva ya que se tienen los simbolos directrices de las producciones de la gramatica
"""

from funciones import simbolosDirectrices

# Terminales
abre_parentesis = '('
cierra_parentesis = ')'
a = 'a'
VT = [a, abre_parentesis, cierra_parentesis]

# No terminales
S = 'S'
B = 'B'
VN = [S, B]

# Producciones
P = {
  S: [[abre_parentesis, B, cierra_parentesis], [a]],
  B: [S]
}

# Cadena de entrada
cadena = 'a'

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

def main(w):
  # Definimos los objetos globales transversales a los procedimientos
  error = Error()
  puntero = Puntero()
  simbolosDirectricesGramatica = simbolosDirectrices({
    'P': P,
    'T': VT,
    'N': VN
  })
  print(simbolosDirectricesGramatica)

  # Comprueba que el puntero ya este "apuntando" al fin de la cadena
  def fin_de_cadena(w):
    return puntero.obtener() == len(w)

  def PNI(VN):
    # Obtiene en que puede derivar VN
    derivaciones = P.get(VN)

    error.desactivar()
    t = puntero.obtener()
    simboloApuntado = w[t]
    # simbolosDirectricesGramatica.get(VN) devuelve los directrices de cada derivacion de VN
    # sd es el simbolo directriz
    # i es el indice de la derivacion a la cual pertenece el simbolo directriz
    # Ejemplo:
    # S -> (B) | a
    # simbolos directrices de S: ['(', 'a']
    # si simboloApuntado es '(' entonces i = 0 ya que '(' pertenece a la primera derivacion
    for i, sd in enumerate(simbolosDirectricesGramatica.get(VN)):
      if simboloApuntado in sd:
        derivacionQueFunciona = derivaciones[i]
        procesar(derivacionQueFunciona)
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