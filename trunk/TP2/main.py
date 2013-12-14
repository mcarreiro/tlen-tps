from parser import * 

import ply.yacc as yacc
yacc.yacc()

def parsearArchivo(ruta):
	cadenas = leerArchivo(ruta)
	for linea in cadenas:
		print linea
		yacc.parse(linea)

def parsearCadena(cadena):
	yacc.parse(cadena)

while 1:
    try:
        # s = input('calc > ')   # Use raw_input on Python 2
  #       s = '''{ 
		#     {{-1;1}.loop(44).expand(2).tune(-1).loop(2.9).fill(3)}.loop(5).post();                                                  
		#     {-1;1}.loop(44).expand(2).loop(6);                            
		#     {-1;1}.loop(44).expand(2).tune(+2).loop(9).fill(9);            
		#     {-1;1}.loop(44).expand(2).tune(-5).loop(3).fill(3);           
		#     {-1;1}.loop(44).expand(2).tune(-1).loop(3).fill(3);            
		#     {-1;1}.loop(44).expand(2).loop(4.5);                           
		#     {-1;1}.loop(44).expand(2).tune(-1).loop(4.5).fill(4.5);        
		#     {-1;1}.loop(44).expand(2).tune(-5).loop(12).fill(12);          
		#     {{-1;1}.loop(44).expand(2).loop(2.9).fill(3)}.loop(2);                                                
		#     {-1;1}.loop(44).expand(2).tune(-3).loop(2.9).fill(3);         
		#     {-1;1}.loop(44).expand(2).loop(4.5);                           
		#     {-1;1}.loop(44).expand(2).tune(-5).loop(5.9).fill(6);         
		#     {-1;1}.loop(44).expand(2).tune(-5).loop(3).fill(3);            
		#     {-1;1}.loop(44).expand(2).loop(3);                            
		#     {-1;1}.loop(44).expand(2).tune(+5).loop(3).fill(3);            
		#     {-1;1}.loop(44).expand(2).tune(+4).loop(2.9).fill(3);         
		#     {-1;1}.loop(44).expand(2).loop(8.9).fill(9)                  
		# }.loop(3).play(300)'''
		s = '{1+2*3}.post()'
    except EOFError:
        break
    yacc.parse(s)
    break


