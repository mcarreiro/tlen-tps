from tokens import *
from funciones import *

precedence = (
    ('right','UMINUS'),
    ('right','SUB','CON'),
    )

def p_s1(t):
	'''s : g'''
	t[0] = t[1]
def p_s2(t):
	'''s : s POINT p'''
	t[0] = method(t[3]['method'],t[1],t[3]['arg1'])
def p_s3(t):
	'''s : s o s '''
	t[0] = oper(t[2],t[1],t[3])

def p_s4(t):
	'''s : LKEY s RKEY'''
	t[0] = t[2]


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
		 | TUNE LPAREN sign FLOAT RPAREN
		 | FILL LPAREN FLOAT RPAREN
		 | REDUCE LPAREN FLOAT RPAREN
		 | EXPAND paramopcional'''
	if len(t) == 3: #Casos POST y EXPAND
		obj = {'method': t[1], 'arg1':t[2]}
		t[0] = obj
	elif len(t) == 6: #CASO TUNE
		obj = {'method': t[1], 'arg1':t[3]*t[4]}
		t[0] = obj
	else: #Casos PLAY, LOOP, FILL, REDUCE
		obj = {'method': t[1], 'arg1':t[3]}
		t[0] = obj

def p_sign(t):
	'''sign : ADD
			| SUB
			| '''
	if len(t) == 2 and t[1] == '-':
		t[0] = -1
	elif len(t) == 2 and t[1] == 'sub':
		print 'Error, sub no puede usarse para indicar un numero negativo'
		exit()
	elif len(t) == 2 and t[1] == 'add':
		print 'Error, add no puede usarse para indicar un numero positivo'
		exit()
	else:
		t[0] = 1


def p_paren(t):
	'''paren : LPAREN RPAREN
			 | '''
	t[0] = None

def p_paramopcional(t):
	'''paramopcional : LPAREN FLOAT RPAREN
					 | '''
	if len(t) == 3:
	   t[0] = t[2]
	else:
	   t[0] = 1

def p_error(t):
	print t
	print("Syntax error at '%s'" % t.value)
