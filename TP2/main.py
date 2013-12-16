from parser import * 

import ply.yacc as yacc
yacc.yacc()

def parsearArchivo(ruta):
	cadena = leerArchivo(ruta)
	yacc.parse(linea)

def parsearCadena(cadena):
	yacc.parse(cadena)

while 1:
    try:
         s = input('calc > ')   # Use raw_input on Python 2
  
    except EOFError:
        break
    yacc.parse(s)
    break


