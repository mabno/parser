from automatas import sino, si, entonces, func, finfunc, finsi, repetir, hasta, equal, leer, mostrar, parentesisI, parentesisD, id, num, oprel, opsuma, opmult, pyc


# Lista que contiene los tokens. El orden debe ser de los más restrictivos a los menos restrictivos
tokens = [sino, si, entonces, func, finfunc, finsi, repetir, hasta, equal, leer, mostrar, parentesisI, parentesisD, id, num, oprel, opsuma, opmult, pyc]

# Lista de duplas (subcadena, token) que devuelve el programa
lista = []


# Función de transición: se le ingresa un autómata, un símbolo de transición y el estado actual, y devuelve el estado siguiente
def funcionTransicion(automata, simboloTransicion, estadoActual):
  # Cada columna está asociada a un símbolo de entrada. Si el símbolo no pertenece al conjunto, toma el valor -1
  columna = automata[0].find(simboloTransicion)
  # Cada fila está asociada a un estado
  fila = automata[1].index(estadoActual)
  # Si el símbolo no pertenece al conjunto de símbolos de entrada
  if columna == -1:
    # Lo mandás al muere
    estadoSiguiente = 'qt'
  else:
    # Cambio de estado al elemento correspondiente de la matriz
    estadoSiguiente = automata[2][fila][columna]
  return estadoSiguiente


# Función que se le pasa un autómata y una cadena y devuelve un vector: (True si la cadena es aceptada por el autómata y False en caso contrario, True si la cadena pertenece al estado trampa del autómata y False en caso contrario)
def verificaAutomata(automata, cadena):
  # Le asigna el estado inicial
  estado = automata[4]
  # Le aplica la función de transición a cada caracter de la cadena
  for caracter in cadena:
    # Cambio de estado
    estado = funcionTransicion(automata, caracter, estado)
    # Si cae en el estado trampa 'qt' termina el ciclo y devuelve (False, True)
    if estado == 'qt':
      return (False, True)
  # Se fija si es aceptado
  if estado in automata[3]:
    # En efecto, es aceptado
    return (True, False)
  else:
    # No es aceptado, pero todavía no se rindió
    return (False, False)


# Función principal que recorre las palabras de una cadena y asigna, de ser posible, un token a cada una. Devuelve e imprime la lista con las duplas
def lexer(cadena):
  i = 0
  j = 0
  # Dinero que le cobramos al usuario por cada caracter introducido que no pertenece al alfabeto
  propina = 0
  # Lista de duplas (subcadena, token) que devuelve la función
  lista_duplas = []
  # Este guarda una dupla aceptada en la iteración previa. Si en la iteración actual no hay tokens vivos, este valor se agrega a lista_duplas
  ultima_dupla_aceptada = ()
  # Agrega un espacio a la cadena para se procese la última subcadena. Ya que estamos, se lo cobramos al usuario
  cadena += ' '
  # Vector con duplas (caracter, posición) tales que el caracter no fue reconocido por ningún autómata. Se omiten los espacios en blanco y los saltos de línea
  advertencias = ()
  # Se recorren todas las subcadenas de la cadena con un único ciclo
  while j <= len(cadena):
    j += 1
    # Subcadena de i a j que se evalúa
    subcadena_evaluada = cadena[i:j]
    # Tiene a todos los tokens tales que la subcadena no cae en el estado trampa
    tokens_vivos = []
    # Tiene a todas las duplas (subcadena, token) tales que la subcadena es aceptada por el token
    duplas_aceptadas = []
    # Se recorren todos los autómatas
    for token in tokens:
      # Vector de booleanos: (Estado aceptato, Estado trampa)
      estadoToken = verificaAutomata(token, subcadena_evaluada)
      # Si Estado trampa == False, esto es, la subcadena no termina en el estado trampa del token
      if not estadoToken[1]:
        # ¡Vamos! ¡El token vive!
        tokens_vivos.append(token)
        # Si Estado aceptado == True, es decir, la subcadena es aceptada por el token
        if estadoToken[0]:
          # Se agrega a la lista de duplas aceptadas
          duplas_aceptadas.append((subcadena_evaluada, token[5]))
        # Queda en el limbo. Acá solo llegan '=' y '!'
        else:
          limbo = True
      # else: RIP token
    # GOOD ENDING: algún token vive y es aceptado
    if duplas_aceptadas != []:
      # Se guarda el primer token que acepta a la subcadena en el vector auxiliar
      ultima_dupla_aceptada = duplas_aceptadas[0]
      # Reestablecemos el orden (por las dudas)
      limbo = False
    # BAD ENDING: se mueren todos los tokens
    elif tokens_vivos == []:
      # Pero la subcadena anterior es aceptada. Aún hay esperanza
      if ultima_dupla_aceptada != ():
        # Se agrega la dupla anterior a la lista de duplas y se salva
        lista_duplas.append(ultima_dupla_aceptada)
        # Se reinicia el vector auxiliar
        ultima_dupla_aceptada = ()
        # Contrarrestamos el incremento para tratar de salvar al caracter que falló. Todos merecen una segunda oportunidad
        j -= 1
      # Si estaba en el limbo cuando murió
      elif limbo:
        # Contrarrestamos el incremento para tratar de salvar al caracter que falló
        j -= 1
        # Advertimos
        advertencias += (cadena[i], i)
        # Reestablecemos el orden
        limbo = False
      # Acá entra cuando encuentra un caracter que no pertenece a los símbolos de entrada de ningún token, por ejemplo ' ', en cuyo caso se hace la vista gorda y el programa sigue con normalidad, pero todo tiene su precio
      else:
        propina += 1
        # Advertimos
        caracter = cadena[i]
        if caracter != ' ' and caracter != '\n':
          advertencias += (caracter, i)
      # Se avanza en la cadena principal
      i = j
    # else: hay tokens vivos que todavían no aceptan la subcadena, en cuyo caso se sigue intentando en la próxima iteración
  # Añadimos el símbolo de fin de cadena
  lista_duplas.append(('#', '#'))

  print('USUARIO: Acá tenés, ' + str(propina) + '. Disfrutalo gil.' + '\nHANNIBAL LEXER: ' + str(advertencias) + '. Estás advertido.')
  return lista_duplas

'''

lista = lexer('Acá se pone cualquier cosa y Lexer cumple con su cometido')

# Casos de prueba
print(funcionTransicion(func, 'f', 'q1'))
print(funcionTransicion(func, 'i', 'q1'))
print(funcionTransicion(func, 'p', 'q0'))
print(funcionTransicion(oprel, '=', 'q0'))
print(funcionTransicion(oprel, '>', 'q0'))
print(funcionTransicion(num, '4', 'q1'))
print(verificaAutomata(func, 'func'))
print(verificaAutomata(func, 'funci'))
print(verificaAutomata(func, 'FUNSION'))
print(lexer('Función Clausura-λ(Q):\n  Hacer L equal Q cuyos elementos son marcables pero ninguno está marcado\n  Mientras en L haya elementos t sin marcar\n    Marcar t\n    Para cada q en f(t,λ) hacer\n      Si q no está en L entonces\n        Agregar q a L sin marcar\n  Retornar L'))
print(lexer('Función Mover:\n  Hacer L igual a Clausura-λ({x en f(t,a): t pertenece a T})\n  Retornar L'))
print(lexer("Algoritmo de pasaje de AEFND-λ a AEFD:\nQ0 iqual Clausura-λ({q0})\nK egual {Q0} donde K' es marcable y Q0 está sin marcar\nMientras haya T en K' sin marcar\n  Marcar T\n  Para cada a en I hacer\n    U iqual Mover(T, a)\n    Si U no está en K' entonces\n      Agregar U a K' sin marcar\n    f'(T,a) equal U\nHacer F' egual {x en K: x no aceptado}"))
print(lexer('func: leer y; x equal 1; Repetir (1+x) hasta que x>=y; Mostrar el resultado; finfuncion'))
print(lexer("Algoritmo de minimización de AFD: Fin equal Falso;\nk equal 0;\nSi Fin == Falso entonces repetir(\n  P equal conjunto de conjuntos de estados k- equivalentes;\n  P' equal conjunto de conjuntos de estados (k+1) equivalentes;\n  Si P != P' entonces\n    P equal P';\n    k equal k+1;\n  Sino\n    Fin equal Verdadero;\n  Finsi;)\nFinsi;\nRetornar P'"))

'''