from parser import * 

import ply.yacc as yacc
yacc.yacc()

def parsearArchivo(ruta):
	cadena = leerArchivo(ruta)
	return cadena

while 1:
	try:
		s = str(raw_input('calc > ') )  # Use raw_input on Python 
		try:
			s = parsearArchivo(s)
			print s
		except:
			print s
	except EOFError:
		break
	yacc.parse(s)


