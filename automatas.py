# Autómata id: La cadena empieza con una letra y solo contiene letras o números
id = [
    # Conjunto de símbolos de entrada
    r'abcdefghijklmnñopqrstuvwxyzáéíóúABCDEFGHIJKLMNÑOPQRSTUVWXYZÁÉÍÓÚαβγδεθλμνπρσφϕωΔΠΣΦΩ0123456789',
    # Conjunto de estados
    ['q0', 'q1', 'qt'],
    # Función de transición en forma de matriz. Cada columna está asociada a un símbolo de entrada, cada fila a un estado actual y cada elemento es el estado siguiente
    [['q1', 'q1', 'q1', 'q1', 'q1', 'q1', 'q1', 'q1', 'q1', 'q1', 'q1', 'q1', 'q1', 'q1', 'q1', 'q1', 'q1', 'q1', 'q1', 'q1', 'q1', 'q1', 'q1', 'q1', 'q1', 'q1', 'q1', 'q1', 'q1', 'q1', 'q1', 'q1', 'q1', 'q1', 'q1', 'q1', 'q1', 'q1', 'q1', 'q1', 'q1', 'q1', 'q1', 'q1', 'q1', 'q1', 'q1', 'q1', 'q1', 'q1', 'q1', 'q1', 'q1', 'q1', 'q1', 'q1', 'q1', 'q1', 'q1', 'q1', 'q1', 'q1', 'q1', 'q1', 'q1', 'q1', 'q1', 'q1', 'q1', 'q1', 'q1', 'q1', 'q1', 'q1', 'q1', 'q1', 'q1', 'q1', 'q1', 'q1', 'q1', 'q1', 'q1', 'q1', 'qt', 'qt', 'qt', 'qt', 'qt', 'qt', 'qt', 'qt', 'qt', 'qt'],
     ['q1', 'q1', 'q1', 'q1', 'q1', 'q1', 'q1', 'q1', 'q1', 'q1', 'q1', 'q1', 'q1', 'q1', 'q1', 'q1', 'q1', 'q1', 'q1', 'q1', 'q1', 'q1', 'q1', 'q1', 'q1', 'q1', 'q1', 'q1', 'q1', 'q1', 'q1', 'q1', 'q1', 'q1', 'q1', 'q1', 'q1', 'q1', 'q1', 'q1', 'q1', 'q1', 'q1', 'q1', 'q1', 'q1', 'q1', 'q1', 'q1', 'q1', 'q1', 'q1', 'q1', 'q1', 'q1', 'q1', 'q1', 'q1', 'q1', 'q1', 'q1', 'q1', 'q1', 'q1', 'q1', 'q1', 'q1', 'q1', 'q1', 'q1', 'q1', 'q1', 'q1', 'q1', 'q1', 'q1', 'q1', 'q1', 'q1', 'q1', 'q1', 'q1', 'q1', 'q1', 'q1', 'q1', 'q1', 'q1', 'q1', 'q1', 'q1', 'q1', 'q1', 'q1'],
     ['qt', 'qt', 'qt', 'qt', 'qt', 'qt', 'qt', 'qt', 'qt', 'qt', 'qt', 'qt', 'qt', 'qt', 'qt', 'qt', 'qt', 'qt', 'qt', 'qt', 'qt', 'qt', 'qt', 'qt', 'qt', 'qt', 'qt', 'qt', 'qt', 'qt', 'qt', 'qt', 'qt', 'qt', 'qt', 'qt', 'qt', 'qt', 'qt', 'qt', 'qt', 'qt', 'qt', 'qt', 'qt', 'qt', 'qt', 'qt', 'qt', 'qt', 'qt', 'qt', 'qt', 'qt', 'qt', 'qt', 'qt', 'qt', 'qt', 'qt', 'qt', 'qt', 'qt', 'qt', 'qt', 'qt', 'qt', 'qt', 'qt', 'qt', 'qt', 'qt', 'qt', 'qt', 'qt', 'qt', 'qt', 'qt', 'qt', 'qt', 'qt', 'qt', 'qt', 'qt', 'qt', 'qt', 'qt', 'qt', 'qt', 'qt', 'qt', 'qt', 'qt', 'qt']],
    # Conjunto de estados aceptados
    {'q1'},
    # Estado inicial
    'q0',
    # Nombre del autómata
    'id'
]

# Autómata num: La cadena solo contiene números
num = [
    # Conjunto de símbolos de entrada
    r'0123456789',
    # Conjunto de estados
    ['q0', 'q1', 'qt'],
    # Función de transición en forma de matriz. Cada columna está asociada a un símbolo de entrada, cada fila a un estado actual y cada elemento es el estado siguiente
    [['q1', 'q1', 'q1', 'q1', 'q1', 'q1', 'q1', 'q1', 'q1', 'q1'],
     ['q1', 'q1', 'q1', 'q1', 'q1', 'q1', 'q1', 'q1', 'q1', 'q1'],
     ['qt', 'qt', 'qt', 'qt', 'qt', 'qt', 'qt', 'qt', 'qt', 'qt']],
    # Conjunto de estados aceptados
    {'q1'},
    # Estado inicial
    'q0',
    # Nombre del autómata
    'num'
]

# Autómata si: Acepta las cadenas: 'si', 'Si'
si = [
    # Conjunto de símbolos de entrada
    r'isS',
    # Conjunto de estados
    ['q0', 'q1', 'q2', 'qt'],
    # Función de transición en forma de matriz. Cada columna está asociada a un símbolo de entrada, cada fila a un estado actual y cada elemento es el estado siguiente
    [['qt', 'q1', 'q1'],
     ['q2', 'qt', 'qt'],
     ['qt', 'qt', 'qt'],
     ['qt', 'qt', 'qt']],
    # Conjunto de estados aceptados
    {'q2'},
    # Estado inicial
    'q0',
    # Nombre del autómata
    'si'
]

# Autómata sino: Acepta las cadenas: 'sino', 'Sino'
sino = [
    # Conjunto de símbolos de entrada
    r'inosS',
    # Conjunto de estados
    ['q0', 'q1', 'q2', 'q3', 'q4', 'qt'],
    # Función de transición en forma de matriz. Cada columna está asociada a un símbolo de entrada, cada fila a un estado actual y cada elemento es el estado siguiente
    [['qt', 'qt', 'qt', 'q1', 'q1'],
     ['q2', 'qt', 'qt', 'qt', 'qt'],
     ['qt', 'q3', 'qt', 'qt', 'qt'],
     ['qt', 'qt', 'q4', 'qt', 'qt'],
     ['qt', 'qt', 'qt', 'qt', 'qt'],
     ['qt', 'qt', 'qt', 'qt', 'qt']],
    # Conjunto de estados aceptados
    {'q4'},
    # Estado inicial
    'q0',
    # Nombre del autómata
    'sino'
]

# Autómata finsi: Acepta las cadenas: 'finsi', 'Finsi', 'finSi', 'FinSi'
finsi = [
    # Conjunto de símbolos de entrada
    r'finsFS',
    # Conjunto de estados
    ['q0', 'q1', 'q2', 'q3', 'q4', 'q5', 'qt'],
    # Función de transición en forma de matriz. Cada columna está asociada a un símbolo de entrada, cada fila a un estado actual y cada elemento es el estado siguiente
    [['q1', 'qt', 'qt', 'qt', 'q1', 'qt'],
     ['qt', 'q2', 'qt', 'qt', 'qt', 'qt'],
     ['qt', 'qt', 'q3', 'qt', 'qt', 'qt'],
     ['qt', 'qt', 'qt', 'q4', 'qt', 'q4'],
     ['qt', 'q5', 'qt', 'qt', 'qt', 'qt'],
     ['qt', 'qt', 'qt', 'qt', 'qt', 'qt'],
     ['qt', 'qt', 'qt', 'qt', 'qt', 'qt']],
    # Conjunto de estados aceptados
    {'q5'},
    # Estado inicial
    'q0',
    # Nombre del autómata
    'finsi'
]

# Autómata entonces: Acepta las cadenas: 'entonces', 'Entonces'
entonces = [
    # Conjunto de símbolos de entrada
    r'cenostE',
    # Conjunto de estados
    ['q0', 'q1', 'q2', 'q3', 'q4', 'q5', 'q6', 'q7', 'q8', 'qt'],
    # Función de transición en forma de matriz. Cada columna está asociada a un símbolo de entrada, cada fila a un estado actual y cada elemento es el estado siguiente
    [['qt', 'q1', 'qt', 'qt', 'qt', 'qt', 'q1'],
     ['qt', 'qt', 'q2', 'qt', 'qt', 'qt', 'qt'],
     ['qt', 'qt', 'qt', 'qt', 'qt', 'q3', 'qt'],
     ['qt', 'qt', 'qt', 'q4', 'qt', 'qt', 'qt'],
     ['qt', 'qt', 'q5', 'qt', 'qt', 'qt', 'qt'],
     ['q6', 'qt', 'qt', 'qt', 'qt', 'qt', 'qt'],
     ['qt', 'q7', 'qt', 'qt', 'qt', 'qt', 'qt'],
     ['qt', 'qt', 'qt', 'qt', 'q8', 'qt', 'qt'],
     ['qt', 'qt', 'qt', 'qt', 'qt', 'qt', 'qt'],
     ['qt', 'qt', 'qt', 'qt', 'qt', 'qt', 'qt']],
    # Conjunto de estados aceptados
    {'q8'},
    # Estado inicial
    'q0',
    # Nombre del autómata
    'entonces'
]

# Autómata func: Acepta las cadenas: 'func', 'Func', 'funcion', 'Funcion', 'función', 'Función'
func = [
    # Conjunto de símbolos de entrada
    r'cfinouóF',
    # Conjunto de estados
    ['q0', 'q1', 'q2', 'q3', 'q4', 'q5', 'q6', 'q7', 'qt'],
    # Función de transición en forma de matriz. Cada columna está asociada a un símbolo de entrada, cada fila a un estado actual y cada elemento es el estado siguiente
    [['qt', 'q1', 'qt', 'qt', 'qt', 'qt', 'qt', 'q1'],
     ['qt', 'qt', 'qt', 'qt', 'qt', 'q2', 'qt', 'qt'],
     ['qt', 'qt', 'qt', 'q3', 'qt', 'qt', 'qt', 'qt'],
     ['q4', 'qt', 'qt', 'qt', 'qt', 'qt', 'qt', 'qt'],
     ['qt', 'qt', 'q5', 'qt', 'qt', 'qt', 'qt', 'qt'],
     ['qt', 'qt', 'qt', 'qt', 'q6', 'qt', 'q6', 'qt'],
     ['qt', 'qt', 'qt', 'q7', 'qt', 'qt', 'qt', 'qt'],
     ['qt', 'qt', 'qt', 'qt', 'qt', 'qt', 'qt', 'qt'],
     ['qt', 'qt', 'qt', 'qt', 'qt', 'qt', 'qt', 'qt']],
    # Conjunto de estados aceptados
    {'q4', 'q7'},
    # Estado inicial
    'q0',
    # Nombre del autómata
    'func'
]

# Autómata finfunc: Acepta las cadenas: 'finfunc', 'Finfunc', 'finfuncion', 'Finfuncion', 'finfunción', 'Finfunción', 'finFunc', 'FinFunc', 'finFuncion', 'FinFuncion', 'finFunción', 'FinFunción'
finfunc = [
    # Conjunto de símbolos de entrada
    r'cfinouóF',
    # Conjunto de estados
    ['q0', 'q1', 'q2', 'q3', 'q4', 'q5', 'q6', 'q7', 'q8', 'q9', 'q10', 'qt'],
    # Función de transición en forma de matriz. Cada columna está asociada a un símbolo de entrada, cada fila a un estado actual y cada elemento es el estado siguiente
    [['qt', 'q1', 'qt', 'qt', 'qt', 'qt', 'qt', 'q1'],
     ['qt', 'qt', 'q2', 'qt', 'qt', 'qt', 'qt', 'qt'],
     ['qt', 'qt', 'qt', 'q3', 'qt', 'qt', 'qt', 'qt'],
     ['qt', 'q4', 'qt', 'qt', 'qt', 'qt', 'qt', 'q4'],
     ['qt', 'qt', 'qt', 'qt', 'qt', 'q5', 'qt', 'qt'],
     ['qt', 'qt', 'qt', 'q6', 'qt', 'qt', 'qt', 'qt'],
     ['q7', 'qt', 'qt', 'qt', 'qt', 'qt', 'qt', 'qt'],
     ['qt', 'qt', 'q8', 'qt', 'qt', 'qt', 'qt', 'qt'],
     ['qt', 'qt', 'qt', 'qt', 'q9', 'qt', 'q9', 'qt'],
     ['qt', 'qt', 'qt', 'q10', 'qt', 'qt', 'qt', 'qt'],
     ['qt', 'qt', 'qt', 'qt', 'qt', 'qt', 'qt', 'qt'],
     ['qt', 'qt', 'qt', 'qt', 'qt', 'qt', 'qt', 'qt']],
    # Conjunto de estados aceptados
    {'q7', 'q10'},
    # Estado inicial
    'q0',
    # Nombre del autómata
    'finfunc'
]

# Autómata repetir: Acepta las cadenas: 'repetir', 'Repetir'
repetir = [
    # Conjunto de símbolos de entrada
    r'eiprtR',
    # Conjunto de estados
    ['q0', 'q1', 'q2', 'q3', 'q4', 'q5', 'q6', 'q7', 'qt'],
    # Función de transición en forma de matriz. Cada columna está asociada a un símbolo de entrada, cada fila a un estado actual y cada elemento es el estado siguiente
    [['qt', 'qt', 'qt', 'q1', 'qt', 'q1'],
     ['q2', 'qt', 'qt', 'qt', 'qt', 'qt'],
     ['qt', 'qt', 'q3', 'qt', 'qt', 'qt'],
     ['q4', 'qt', 'qt', 'qt', 'qt', 'qt'],
     ['qt', 'qt', 'qt', 'qt', 'q5', 'qt'],
     ['qt', 'q6', 'qt', 'qt', 'qt', 'qt'],
     ['qt', 'qt', 'qt', 'q7', 'qt', 'qt'],
     ['qt', 'qt', 'qt', 'qt', 'qt', 'qt'],
     ['qt', 'qt', 'qt', 'qt', 'qt', 'qt']],
    # Conjunto de estados aceptados
    {'q7'},
    # Estado inicial
    'q0',
    # Nombre del autómata
    'repetir'
]

# Autómata hasta: Acepta las cadenas: 'hasta', 'Hasta'
hasta = [
    # Conjunto de símbolos de entrada
    r'ahstH',
    # Conjunto de estados
    ['q0', 'q1', 'q2', 'q3', 'q4', 'q5', 'qt'],
    # Función de transición en forma de matriz. Cada columna está asociada a un símbolo de entrada, cada fila a un estado actual y cada elemento es el estado siguiente
    [['qt', 'q1', 'qt', 'qt', 'q1'],
     ['q2', 'qt', 'qt', 'qt', 'qt'],
     ['qt', 'qt', 'q3', 'qt', 'qt'],
     ['qt', 'qt', 'qt', 'q4', 'qt'],
     ['q5', 'qt', 'qt', 'qt', 'qt'],
     ['qt', 'qt', 'qt', 'qt', 'qt'],
     ['qt', 'qt', 'qt', 'qt', 'qt']],
    # Conjunto de estados aceptados
    {'q5'},
    # Estado inicial
    'q0',
    # Nombre del autómata
    'hasta'
]

# Autómata equal: Acepta las cadenas: 'equal', 'iqual', 'Equal', 'Iqual', 'egual', 'igual', 'Egual', 'Igual'
equal = [
    # Conjunto de símbolos de entrada
    r'ageilquEI',
    # Conjunto de estados
    ['q0', 'q1', 'q2', 'q3', 'q4', 'q5', 'qt'],
    # Función de transición en forma de matriz. Cada columna está asociada a un símbolo de entrada, cada fila a un estado actual y cada elemento es el estado siguiente
    [['qt', 'qt', 'q1', 'q1', 'qt', 'qt', 'qt', 'q1', 'q1'],
     ['qt', 'q2', 'qt', 'qt', 'qt', 'q2', 'qt', 'qt', 'qt'],
     ['qt', 'qt', 'qt', 'qt', 'qt', 'qt', 'q3', 'qt', 'qt'],
     ['q4', 'qt', 'qt', 'qt', 'qt', 'qt', 'qt', 'qt', 'qt'],
     ['qt', 'qt', 'qt', 'qt', 'q5', 'qt', 'qt', 'qt', 'qt'],
     ['qt', 'qt', 'qt', 'qt', 'qt', 'qt', 'qt', 'qt', 'qt'],
     ['qt', 'qt', 'qt', 'qt', 'qt', 'qt', 'qt', 'qt', 'qt']],
    # Conjunto de estados aceptados
    {'q5'},
    # Estado inicial
    'q0',
    # Nombre del autómata
    'equal'
]

# Autómata leer: Acepta las cadenas: 'leer', 'Leer'
leer = [
    # Conjunto de símbolos de entrada
    r'elrL',
    # Conjunto de estados
    ['q0', 'q1', 'q2', 'q3', 'q4', 'qt'],
    # Función de transición en forma de matriz. Cada columna está asociada a un símbolo de entrada, cada fila a un estado actual y cada elemento es el estado siguiente
    [['qt', 'q1', 'qt', 'q1'],
     ['q2', 'qt', 'qt', 'qt'],
     ['q3', 'qt', 'qt', 'qt'],
     ['qt', 'qt', 'q4', 'qt'],
     ['qt', 'qt', 'qt', 'qt'],
     ['qt', 'qt', 'qt', 'qt']],
    # Conjunto de estados aceptados
    {'q4'},
    # Estado inicial
    'q0',
    # Nombre del autómata
    'leer'
]

# Autómata mostrar: Acepta las cadenas: 'mostrar', 'Mostrar'
mostrar = [
    # Conjunto de símbolos de entrada
    r'amorstM',
    # Conjunto de estados
    ['q0', 'q1', 'q2', 'q3', 'q4', 'q5', 'q6', 'q7', 'qt'],
    # Función de transición en forma de matriz. Cada columna está asociada a un símbolo de entrada, cada fila a un estado actual y cada elemento es el estado siguiente
    [['qt', 'q1', 'qt', 'qt', 'qt', 'qt', 'q1'],
     ['qt', 'qt', 'q2', 'qt', 'qt', 'qt', 'qt'],
     ['qt', 'qt', 'qt', 'qt', 'q3', 'qt', 'qt'],
     ['qt', 'qt', 'qt', 'qt', 'qt', 'q4', 'qt'],
     ['qt', 'qt', 'qt', 'q5', 'qt', 'qt', 'qt'],
     ['q6', 'qt', 'qt', 'qt', 'qt', 'qt', 'qt'],
     ['qt', 'qt', 'qt', 'q7', 'qt', 'qt', 'qt'],
     ['qt', 'qt', 'qt', 'qt', 'qt', 'qt', 'qt'],
     ['qt', 'qt', 'qt', 'qt', 'qt', 'qt', 'qt']],
    # Conjunto de estados aceptados
    {'q7'},
    # Estado inicial
    'q0',
    # Nombre del autómata
    'mostrar'
]

# Autómata parentesisI: La cadena es el paréntesis izquierdo '('
parentesisI = [
    # Conjunto de símbolos de entrada
    r'(',
    # Conjunto de estados
    ['q0', 'q1', 'qt'],
    # Función de transición en forma de matriz. Cada columna está asociada a un símbolo de entrada, cada fila a un estado actual y cada elemento es el estado siguiente
    [['q1'],
     ['qt'],
     ['qt']],
    # Conjunto de estados aceptados
    {'q1'},
    # Estado inicial
    'q0',
    # Nombre del autómata
    '('
]

# Autómata parentesisD: La cadena es el paréntesis derecho ')'
parentesisD = [
    # Conjunto de símbolos de entrada
    r')',
    # Conjunto de estados
    ['q0', 'q1', 'qt'],
    # Función de transición en forma de matriz. Cada columna está asociada a un símbolo de entrada, cada fila a un estado actual y cada elemento es el estado siguiente
    [['q1'],
     ['qt'],
     ['qt']],
    # Conjunto de estados aceptados
    {'q1'},
    # Estado inicial
    'q0',
    # Nombre del autómata
    ')'
]

# Autómata oprel: La cadena es un operador relacional: '==', '<=', '>=', '<', '>', '!='
oprel = [
    # Conjunto de símbolos de entrada
    r'!<=>',
    # Conjunto de estados
    ['q0', 'q1', 'q2', 'q3', 'qt'],
    # Función de transición en forma de matriz. Cada columna está asociada a un símbolo de entrada, cada fila a un estado actual y cada elemento es el estado siguiente
    [['q1', 'q2', 'q1', 'q2'],
     ['qt', 'qt', 'q3', 'qt'],
     ['qt', 'qt', 'q3', 'qt'],
     ['qt', 'qt', 'qt', 'qt'],
     ['qt', 'qt', 'qt', 'qt']],
    # Conjunto de estados aceptados
    {'q2', 'q3'},
    # Estado inicial
    'q0',
    # Nombre del autómata
    'oprel'
]

# Autómata opsuma: La cadena es un operador suma: '+', '-'
opsuma = [
    # Conjunto de símbolos de entrada
    r'+-',
    # Conjunto de estados
    ['q0', 'q1', 'qt'],
    # Función de transición en forma de matriz. Cada columna está asociada a un símbolo de entrada, cada fila a un estado actual y cada elemento es el estado siguiente
    [['q1', 'q1'],
     ['qt', 'qt'],
     ['qt', 'qt']],
    # Conjunto de estados aceptados
    {'q1'},
    # Estado inicial
    'q0',
    # Nombre del autómata
    'opsuma'
]

# Autómata opmult: La cadena es un operador multiplicador: '*'
opmult = [
    # Conjunto de símbolos de entrada
    r'*',
    # Conjunto de estados
    ['q0', 'q1', 'qt'],
    # Función de transición en forma de matriz. Cada columna está asociada a un símbolo de entrada, cada fila a un estado actual y cada elemento es el estado siguiente
    [['q1'],
     ['qt'],
     ['qt']],
    # Conjunto de estados aceptados
    {'q1'},
    # Estado inicial
    'q0',
    # Nombre del autómata
    'opmult'
]

# Autómata pyc: La cadena es un punto y coma: ';'
pyc = [
    # Conjunto de símbolos de entrada
    r';',
    # Conjunto de estados
    ['q0', 'q1', 'qt'],
    # Función de transición en forma de matriz. Cada columna está asociada a un símbolo de entrada, cada fila a un estado actual y cada elemento es el estado siguiente
    [['q1'],
     ['qt'],
     ['qt']],
    # Conjunto de estados aceptados
    {'q1'},
    # Estado inicial
    'q0',
    # Nombre del autómata
    ';'
]
