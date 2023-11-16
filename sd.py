"""
 'T': ['sino', 'si', 'entonces', 'func', 'finfunc', 'finsi', 'repetir', 'hasta', 'equal', 'leer',
          'mostrar', '(', ')', 'id', 'num', 'oprel', 'opsuma', 'opmult', ';'],
    # No terminales
    'N': ['Program', 'ListaSentencias', "ListaSentencias'", 'Sentencia', 'SentenciaSi', "SentenciaSi'", "SentenciaSi''", "SentenciaSi'''", 'SentenciaFun', 'SentenciaAsig',
          'SentenciaLeer', 'SentenciaMostrar', 'SentenciaRepetir', 'Proc', 'ListaPar', "ListaPar'", 'Expresion', "Expresion'", 'Expresion2', "Expresion2'", 'Factor', 'Termino', "Termino'"],
"""

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

    
    'SentenciaSi' : {"si" : ["si", 'Expresion', "token_entonces", 'ListaSentencias', 'SentenciaSiPrima']},
    
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
    
    'ExpresionPrima' : {"sino" : [], "token_entonces" : [], "finsi" : [], "finfunc" : [],
                   "hasta" : [], "oprel" : ["oprel", 'Expresion2'], ")" : [],
                ";" : [],'#':[]},
    
    'Expresion2' : {"id" : ['Termino', 'Expresion2Prima'], "num" : ['Termino', 'Expresion2Prima'],
                    "(" : ['Termino', 'Expresion2Prima']},
    
    'Expresion2Prima' : {"sino" : [], "token_entonces" : [], "finsi" : [], "finfunc" : [],
                "hasta" : [], "oprel" : [], ")" : [],
                ";" : [] , "opsuma" : ["opsuma", 'Termino', 'Expresion2Prima'],'#':[] },
    
    'Factor' : {"id" : ["id"], "num" : ["num"],
                "(" : ["(", 'Expresion', ")"]},
    
    'Termino' : {"id" : ['Factor', 'TerminoPrima'], "num" : ['Factor', 'TerminoPrima'],
                 "(" : ['Factor', 'TerminoPrima']},
    
    'TerminoPrima' : {"sino" : [], "token_entonces" : [], "finsi" : [], "finfunc" : [],
                        "hasta" : [],"oprel" : [],")" : [],
                        ";" : [] , "opsuma" : [], "opmult" : ["opmult", 'Factor', 'TerminoPrima'],'#':[]}
            
                        
}