from automatas import sino, si, entonces, func, finfunc, finsi, repetir, hasta, equal, leer, mostrar, parentesisI, parentesisD, id, num, oprel, opsuma, opmult, pyc

# Cadena vacía (lambdita)
λ = ""


# Función que convierte los terminales de una gramática a texto
# Conviene usarla para imprimir la gramática
def terminalesToString(gramatica):
    # Se crea una lista con los terminales de la gramática como texto
    terminales = []
    for terminal in gramatica['T']:
        terminales.append(terminal[5])
    # Se crea un diccionario con las producciones de la gramática con los terminales de las derivaciones como texto
    producciones = {}
    for produccion in gramatica['P']:
        producciones.update({produccion: []})
        posicion = 0
        for derivacion in gramatica['P'][produccion]:
            producciones[produccion].append([])
            for simbolo in derivacion:
                # posicion = derivacion.index(simbolo)
                if isinstance(simbolo, str):
                    producciones[produccion][posicion].append(simbolo)
                else:
                    producciones[produccion][posicion].append(simbolo[5])
            posicion += 1
        nuevaGramatica = {
            'T': terminales, 'N': gramatica['N'], 'P': producciones, 'S': gramatica['S']}
    return nuevaGramatica


# Función que elimina por completo la recursividad izquierda de una gramática
# Sacado de los apuntes de la cátedra
def eliminarRecursividadIzquierda(gramatica):
    # Se crea una copia de la gramática original
    gramaticaSRI = {
        'T': gramatica['T'], 'N': gramatica['N'], 'P': {}, 'S': gramatica['S']}
    # No terminales: A1, A2, ..., An
    n = len(gramatica['N'])
    for i in range(0, n):
        Ai = gramatica['N'][i]
        gramaticaSRI['P'].update({Ai: []})
        for j in range(i):
            Aj = gramatica['N'][j]
            # Si Ai -> Ajγ
            if gramatica['P'][Ai][0] == Aj:
                γ = gramatica['P'][Ai][1:]
                # Se sustituye cada producción Ai -> Ajγ por Ai -> δ1γ | δ2γ | ... | δkγ, donde Aj -> δ1 | δ2 | ... | δk
                for derivacion in gramatica['P'][Aj]:
                    gramaticaSRI['P'][Ai].append(derivacion + γ)
        # Se elimina la recursividad izquierda directa en Ai
        # Se crea una nueva producción Ai'
        AiNueva = Ai + "\'"
        gramaticaSRI['N'].append(AiNueva)
        gramaticaSRI['P'].update({AiNueva: [[λ]]})
        for derivacion in gramatica['P'][Ai]:
            # Si Ai -> Aiα
            if derivacion[0] == Ai:
                α = derivacion[1:]
                nuevaDerivacion = α.copy()
                nuevaDerivacion.append(AiNueva)
                gramaticaSRI['P'][AiNueva].append(α)
            # Si Ai -> β y β no comienza con Ai
            else:
                nuevaDerivacion = derivacion.copy()
                nuevaDerivacion.append(AiNueva)
                gramaticaSRI['P'][Ai].append(nuevaDerivacion)
    return gramaticaSRI


# Función que factoriza una gramática
# Hecha por github copilot
def factorizar(gramatica):
    # Se crea una copia de la gramática original
    gramaticaF = {
        'T': gramatica['T'], 'N': gramatica['N'], 'P': {}, 'S': gramatica['S']}
    # No terminales: A1, A2, ..., An
    n = len(gramatica['N'])
    for i in range(0, n):
        Ai = gramatica['N'][i]
        gramaticaF['P'].update({Ai: []})
        # Para cada producción Ai -> α1 | α2 | ... | αk
        for derivacion in gramatica['P'][Ai]:
            # Si α1 = α2 = ... = αk = λ
            if derivacion == [λ]:
                gramaticaF['P'][Ai].append(derivacion)
            else:
                # Si α1 = βγ1 y α2 = βγ2 y ... y αk = βγk
                # Se factoriza la producción Ai -> βAi' y se agregan las producciones Ai' -> γ1 | γ2 | ... | γk
                # gramaticaF['P'][Ai].append(derivacion)
                pass
    return gramaticaF


# Gramática posta LL(1)
gramatica = {
    # Terminales
    'T': [sino, si, entonces, func, finfunc, finsi, repetir, hasta, equal, leer,
          mostrar, parentesisI, parentesisD, id, num, oprel, opsuma, opmult, pyc],
    # No terminales
    'N': ['Program', 'ListaSentencias', "ListaSentencias'", 'Sentencia', 'SentenciaSi', "SentenciaSi'", "SentenciaSi''", "SentenciaSi'''", 'SentenciaFun', 'SentenciaAsig',
          'SentenciaLeer', 'SentenciaMostrar', 'Proc', 'ListaPar', "ListaPar'", 'Expresion', "Expresion'", 'Expresion2', "Expresion2'", 'Factor', 'Termino', "Termino'"],
    # Producciones
    'P': {
        'Program': [['ListaSentencias']],
        'ListaSentencias': [['Sentencia', "ListaSentencias'"]],
        "ListaSentencias'": [[λ], [pyc, 'Sentencia']],
        'Sentencia': [['SentenciaSi'], ['SentenciaFun'], ['SentenciaAsig'], ['SentenciaLeer'], ['SentenciaMostrar']],
        'SentenciaSi': [["SentenciaSi'", 'ListaSentencias', finsi]],
        "SentenciaSi'": [[si, 'Expresion', entonces, "SentenciaSi''"]],
        "SentenciaSi''": [['Sentencia', "SentenciaSi'''"]],
        "SentenciaSi'''": [[λ], [sino, 'Sentencia']],
        'SentenciaFun': [[func, 'Proc', finfunc]],
        'SentenciaAsig': [[id, equal, 'Expresion']],
        'SentenciaLeer': [[leer, id]],
        'SentenciaMostrar': [[mostrar, 'Expresion']],
        'Proc': [[id, parentesisI, 'ListaPar', parentesisD, 'ListaSentencias']],
        'ListaPar': [[id, "ListaPar'"]],
        "ListaPar'": [[λ], [pyc, id, "ListaPar'"]],
        'Expresion': [["Expresion'", 'Expresion2']],
        "Expresion'": [[λ], ['oprel', 'Expresion2']],
        'Expresion2': [['Termino', "Expresion2'"]],
        "Expresion2'": [[λ], [opsuma, 'Termino']],
        'Termino': [['Factor', "Termino'"]],
        "Termino'": [[λ], [opmult, 'Factor']],
        'Factor': [[parentesisI, 'Expresion', parentesisD], [id], [num]]
    },
    # Símbolo distinguido
    'S': 'Program'
}

# Gramática posta LL(1) con los terminales como texto (para pruebas)
gramaticaSTR = {
    # Terminales
    'T': ['sino', 'si', 'entonces', 'func', 'finfunc', 'finsi', 'repetir', 'hasta', 'equal', 'leer',
          'mostrar', '(', ')', 'id', 'num', 'oprel', 'opsuma', 'opmult', ';'],
    # No terminales
    'N': ['Program', 'ListaSentencias', "ListaSentencias'", 'Sentencia', 'SentenciaSi', "SentenciaSi'", "SentenciaSi''", "SentenciaSi'''", 'SentenciaFun', 'SentenciaAsig',
          'SentenciaLeer', 'SentenciaMostrar', 'Proc', 'ListaPar', "ListaPar'", 'Expresion', "Expresion'", 'Expresion2', "Expresion2'", 'Factor', 'Termino', "Termino'"],
    # Producciones
    'P': {
        'Program': [['ListaSentencias']],
        'ListaSentencias': [['Sentencia', "ListaSentencias'"]],
        "ListaSentencias'": [[λ], [';', 'Sentencia']],
        'Sentencia': [['SentenciaSi'], ['SentenciaFun'], ['SentenciaAsig'], ['SentenciaLeer'], ['SentenciaMostrar']],
        'SentenciaSi': [["SentenciaSi'", 'ListaSentencias', 'finsi']],
        "SentenciaSi'": [['si', 'Expresion', 'entonces', "SentenciaSi''"]],
        "SentenciaSi''": [['Sentencia', "SentenciaSi'''"]],
        "SentenciaSi'''": [[λ], ['sino', 'Sentencia']],
        'SentenciaFun': [['func', 'Proc', 'finfunc']],
        'SentenciaAsig': [['id', 'equal', 'Expresion']],
        'SentenciaLeer': [['leer', 'id']],
        'SentenciaMostrar': [['mostrar', 'Expresion']],
        'Proc': [['id', '(', 'ListaPar', ')', 'ListaSentencias']],
        'ListaPar': [['id', "ListaPar'"]],
        "ListaPar'": [[λ], [';', 'id', "ListaPar'"]],
        'Expresion': [["Expresion'", 'Expresion2']],
        "Expresion'": [[λ], ['oprel', 'Expresion2']],
        'Expresion2': [['Termino', "Expresion2'"]],
        "Expresion2'": [[λ], ['opsuma', 'Termino']],
        'Termino': [['Factor', "Termino'"]],
        "Termino'": [[λ], ['opmult', 'Factor']],
        'Factor': [['(', 'Expresion', ')'], ['id'], ['num']]
    },
    # Símbolo distinguido
    'S': 'Program'
}
