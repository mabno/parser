from Parser import simbolosDirectrices, cadenizacion, primeros, siguientes, λ
from automatas import sino, si, entonces, func, finfunc, finsi, repetir, hasta, equal, leer, mostrar, parentesisI, parentesisD, id, num, oprel, opsuma, opmult, pyc
from gramaticas import gramatica, gramaticaSTR

VN = gramaticaSTR['N']

VT = gramaticaSTR['T']

P = gramaticaSTR['P']

'''
def lex(codigo_fuente):
    lista_tokens=[]
    for i in codigo_fuente:
        if i in gramatica['T']:
            lista_tokens.append((cadenizacion(i),cadenizacion(i)))
        else:
            return []
    lista_tokens.append(('Eof','Eof'))
    return lista_tokens
'''

def desc_rec_proc(codigo_fuente):
    datos_locales = {
        'lista_tokens': codigo_fuente,
        'index': 0,
        'error': False,
    }   
          
    def pni(no_terminal):
        for cuerpo_produccion in P[no_terminal]:
            backtracking_index = datos_locales['index']
            procesar(cuerpo_produccion)
            if datos_locales['error']:
                datos_locales['index'] = backtracking_index
            else:
                break
    
    def procesar(cuerpo_produccion):
        for simbolo in cuerpo_produccion:
            caracter_actual = datos_locales['lista_tokens'][datos_locales['index']][1]
            #lexema_actual = datos_locales['lista_tokens'][datos_locales['index']][0]
            datos_locales['error'] = False
            if simbolo in VT:
                if simbolo == caracter_actual:
                    datos_locales['index'] += 1                        
                else:
                    datos_locales['error'] = True
                    break
            elif simbolo in VN:
                pni(simbolo)
                if datos_locales['error']:
                    break
                
    
    def principal():
        pni(gramatica['S'])
        caracter_actual = datos_locales['lista_tokens'][datos_locales['index']][0]
        if caracter_actual != 'Eof' or datos_locales['error']:
            print('La cadena no pertenece al lenguaje')
            return False
        print('La cadena pertenece al lenguaje')
        return True
    
    return principal()

print(desc_rec_proc([('variable', 'id'), ('igual', 'equal'), ('5', 'num'), ('Eof', 'Eof')]))