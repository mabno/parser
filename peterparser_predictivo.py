from lexer import lexer

"""
  Implementación procedural de analizador sintáctico descendente predictivo.
  Esta version es predictiva ya que se tienen los simbolos directrices de las producciones de la gramatica
"""

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


# Gramática posta LL(1) con los terminales como texto

SD = { 
    'Program' : {"si" : ['ListaSentencias'],"func" : ['ListaSentencias'],
                 "repetir" : ['ListaSentencias'], "leer" : ['ListaSentencias'],
                "mostrar" : ['ListaSentencias'],"id" : ['ListaSentencias']},
                 
    
    'ListaSentencias' : {"si" : ['Sentencia','ListaSentenciasPrima'],
                 "func" : ['Sentencia','ListaSentenciasPrima'], "repetir" : ['Sentencia','ListaSentenciasPrima'],
                  "leer" : ['Sentencia','ListaSentenciasPrima'], "mostrar" : ['Sentencia','ListaSentenciasPrima'],
                 "id" : ['Sentencia','ListaSentenciasPrima']},
    
    'ListaSentenciasPrima' : { "sino" : [], "finsi" : [], "finfunc" : [''],
                 "hasta" : [], ";" : [";", 'Sentencia', 'ListaSentenciasPrima'],'#':[]},
    
    'Sentencia' : {"si" : ['SentenciaSi'],"func" : ['SentenciaFun'], "repetir" : ['SentenciaRepetir'],
                   "leer" : ['SentenciaLeer'], "mostrar" : ['SentenciaMostrar'],
                 "id" : ['SentenciaAsig']},

    
    'SentenciaSi' : {"si" : ["si", 'Expresion', "entonces", 'ListaSentencias', 'SentenciaSiPrima']},
    
    'SentenciaSiPrima' : { "sino" : ["sino", 'ListaSentencias', "finsi"], "finsi" : ["finsi"]},
    
    'SentenciaRepetir' : { "repetir" : ["repetir", 'ListaSentencias', "hasta", 'Expresion']},
    
    'SentenciaAsig' : {"id" : ["id", "equal", 'Expresion']},
      
    'SentenciaLeer' : { "leer" : ["leer", "id"]},
       
    'SentenciaMostrar' : {"mostrar" : ["mostrar", 'Expresion']},
    
    'SentenciaFun' : {"func" : ["func", 'Proc', "finfunc"]},
    
    'Proc' : {"id" : ["id", "(", 'ListaPar', ")", 'ListaSentencias']},
    
    'ListaPar' : {"id" : ["id", 'ListaParPrima']},
    
    'ListaParPrima' : {")" : [],";" : [";", "id" ,'ListaParPrima']},
    
    'Expresion' : {"id" : ['Expresion2', 'ExpresionPrima'], "num" : ['Expresion2', 'ExpresionPrima'],
                 "(" : ['Expresion2', 'ExpresionPrima']},
    
    'ExpresionPrima' : {"sino" : [], "entonces" : [], "finsi" : [], "finfunc" : [],
                   "hasta" : [], "oprel" : ["oprel", 'Expresion2'], ")" : [],
                ";" : [],'#':[]},
    
    'Expresion2' : {"id" : ['Termino', 'Expresion2Prima'], "num" : ['Termino', 'Expresion2Prima'],
                    "(" : ['Termino', 'Expresion2Prima']},
    
    'Expresion2Prima' : {"sino" : [], "entonces" : [], "finsi" : [], "finfunc" : [],
                "hasta" : [], "oprel" : [], ")" : [],
                ";" : [] , "opsuma" : ["opsuma", 'Termino', 'Expresion2Prima'],'#':[] },
    
    'Factor' : {"id" : ["id"], "num" : ["num"],
                "(" : ["(", 'Expresion', ")"]},
    
    'Termino' : {"id" : ['Factor', 'TerminoPrima'], "num" : ['Factor', 'TerminoPrima'],
                 "(" : ['Factor', 'TerminoPrima']},
    
    'TerminoPrima' : {"sino" : [], "entonces" : [], "finsi" : [], "finfunc" : [],
                        "hasta" : [],"oprel" : [],")" : [],
                        ";" : [] , "opsuma" : [], "opmult" : ["opmult", 'Factor', 'TerminoPrima'],'#':[]}
            
                        
}

no_terminales = ['Program','ListaSentencias','ListaSentenciasPrima', 'Sentencia', 'SentenciaSi', 'SentenciaSiPrima',
                 'SentenciaRepetir', 'SentenciaAsig', 'SentenciaLeer', 'SentenciaMostrar',
                 'SentenciaFun', 'Proc', 'ListaPar', 'ListaParPrima', 'Expresion', 'ExpresionPrima', 'Expresion2', 'Expresion2Prima',
                 'Factor', 'Termino', 'TerminoPrima']

terminales = ["si","sino","entonces","finsi","finfunc",
              "func","repetir","hasta","leer","mostrar",
              "equal","id","num","oprel","(",
              ")",";","opsuma","opmult",'#']

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


def main(cadena):
  # Definimos los objetos globales transversales a los procedimientos
  error = Error()
  puntero = Puntero()

  # Comprueba que el puntero ya este "apuntando" al fin de la cadena
  def fin_de_cadena(cadena):
    return cadena[puntero.obtener()] == '#'

  def PNI(noTerminal):
    #derivaciones = []
    # Obtiene en que puede derivar el no terminal
    #derivaciones = gramatica['P'][noTerminal]


    error.desactivar()
    t = puntero.obtener()


    simboloApuntado = cadena[t]
    # simbolosDirectricesGramatica.get(VN) devuelve los directrices de cada derivacion de VN
    # sd es el simbolo directriz
    # i es el indice de la derivacion a la cual pertenece el simbolo directriz
    # Ejemplo:
    # S -> (B) | a
    # simbolos directrices de S: ['(', 'a']
    # si simboloApuntado es '(' entonces i = 0 ya que '(' pertenece a la primera derivacion
    if simboloApuntado in SD[noTerminal].keys():
      parteDerecha = SD [noTerminal][simboloApuntado] 
      procesar(parteDerecha)
    else:
      error.activar()
      return

  def procesar(produccion):
    for j in range(0, len(produccion)):
      t = puntero.obtener()
      # Obtengo el simbolo de la produccion en la posicion j
      xj = produccion[j]
      # Si es un terminal
      if xj in terminales:

        if cadena[t] == xj:
          puntero.avanzar()
        else:
          error.activar()
          break
      # Si es un no terminal
      if xj in no_terminales:

        PNI(xj)
        if error.obtener():
          break

  PNI('Program')
  if not error.obtener() and fin_de_cadena(cadena):
    print('PETER PARSER: Cadena aceptada')
  else:
    print('PETER PARSER: Cadena rechazada. No se puede derivar en el terminal "' + str(lista[puntero.obtener()]) + '" de la posición ' + str(puntero.obtener()) + '.')


# Pruebas

# Cadena de texto de entrada
#cadena = 'si vgAuxi==7, entonces vgAuxi igual 1, sino leer libro. FinSi.'
cadena = "si 6>7 entonces leer id finsi"
# Lista de tokens devuelta por Hannibal Lexer
lista = [token[1] for token in lexer(cadena)]
print('Cadena de tokens: ' + str(lista))
main(lista)

# Cadena de texto de entrada
cadena = 'función y(x): y equal (x * 2) + 3. Finfunción;\nz iqual y'
# Lista de tokens devuelta por Hannibal Lexer
lista = [token[1] for token in lexer(cadena)]
print('Cadena de tokens: ' + str(lista))
main(lista)

# Cadena de texto de entrada
cadena = 'si vgAuxi == 7 entonces vgAuxi equal 1 sino mostrar demostración. FinSi.'
# Lista de tokens devuelta por Hannibal Lexer
lista = [token[1] for token in lexer(cadena)]
print('Cadena de tokens: ' + str(lista))
main(lista)

# Cadena de texto de entrada
cadena = 'func y(x) leer y finfuncion; Repetir x equal x + 1 hasta x>=y.'
# Lista de tokens devuelta por Hannibal Lexer
lista = [token[1] for token in lexer(cadena)]
print('Cadena de tokens: ' + str(lista))
main(lista)