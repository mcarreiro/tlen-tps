from tokens import *
from funciones import *

precedence = (
    ('left','ADD','SUB'),
    ('left','MUL','DIV'),
    ('left','CON','SUB'),
    ('right','UMINUS'),
    )

def p_s(t):
	'''s : LKEY s RKEY a
		 | g a'''

	if len(t) == 3: #Caso G A		
		a = t[2]
		res = t[1]
		if res != None and a !=None: #Caso Generador y Resto Operador
			while a != None:
				if len(a) == 3: #Caso methodo
					res = method(a['method'],res,a['arg1'])
					a = a['rest']
				elif len(a) == 2: #Caso operador
					res = oper(a['operator'],res,a['value'])
					print res
					a = None
				else: #Caso Vacio
					a = None
			t[0] = res
		else:#Caso Generador y NO Operador
			t[0] = t[1]
	else: #Caso {S}A
		a = t[4]
		res = t[2]
		if res != None:
			while a != None:
				if len(a) == 3: #Caso methodo
					res = method(a['method'],res,a['arg1'])
					a = a['rest']
				elif len(a) == 2: #Caso operador
					res = oper(a['operator'],res,a['value'])
					a = None
				else: #Caso Vacio
					a = None

			t[0] = res

def p_a(t):
	'''a : POINT p a 
		 | b'''
	if t[1] != '.':
		t[0] = t[1]
	else:
		obj = {'method': t[2]['method'],'arg1':t[2]['arg1'], 'rest': t[3]}
		t[0] = obj

def p_b(t):
	'''b : o s
		 | '''
	if len(t) > 1:
		obj = {'operator': t[1], 'value': t[2]}
		t[0] = obj
			
def p_g(t):
	'''g : SIN LPAREN FLOAT COMA FLOAT RPAREN
		 | LIN LPAREN FLOAT COMA FLOAT RPAREN
		 | SIL paren
		 | NOI LPAREN FLOAT RPAREN
		 | SUB FLOAT %prec UMINUS
		 | FLOAT'''
	if t[1] == 'sin':
		t[0] = sin(t[3],t[5])
	elif t[1] == 'lin':
		t[0] = lin(t[3],t[5])
	elif t[1] == 'sil':
		t[0] = sil()
	elif t[1] == 'noi':
		t[0] = noi(t[3])
	elif t[1] == '-':
		t[0] = [-t[2]]
	elif t[1] == 'sub':
		print 'Error, sub no puede usarse para indicar un numero negativo'
		exit()
	else:
		t[0] = [t[1]]

def p_o(t):
	'''o : CON
		| MIX
		| ADD
		| SUB
		| MUL
		| DIV'''
	t[0] = t[1]

def p_p(t):
	'''p : PLAY LPAREN FLOAT RPAREN
		 | POST paren
		 | LOOP LPAREN FLOAT RPAREN
		 | TUNE LPAREN FLOAT RPAREN
		 | FILL LPAREN FLOAT RPAREN
		 | REDUCE LPAREN FLOAT RPAREN
		 | EXPAND LPAREN FLOAT RPAREN'''
	if len(t) == 3: #Casos POST
		obj = {'method': t[1], 'arg1':None}
		t[0] = obj
	else: #Casos PLAY, LOOP, TUNE, FILL, REDUCE y EXPAND
		obj = {'method': t[1], 'arg1':t[3]}
		t[0] = obj

# def p_sign(t):
# 	'''sign : POSITIVE
# 			| NEGATIVE
# 			| '''
# 	if len(t) == 2 and t[1] == '-':
# 		print t[1]
# 		t[0] = -1
# 	else:
# 		t[0] = 1


def p_paren(t):
	'''paren : LPAREN RPAREN
			 | '''

def p_error(t):
	print("Syntax error at '%s'" % t.value)
