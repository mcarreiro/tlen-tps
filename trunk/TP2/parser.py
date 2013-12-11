from tokens import *
from funciones import *

def p_s(t):
	'''s : LKEY s RKEY a
		 | g b'''

	if len(t) == 3:		
		if t[1] != None and t[2] != None:
			t[0] = oper(t[2]['operator'],t[1],t[2]['value'])
		elif t[1] != None and t[2] == None:
			t[0] = t[1]
		else:
			pass
	else:
		pass

	print t[0]
	

def p_a(t):
	'''a : POINT p a 
		 | b'''
	if t[1] != '.':
		t[0] = t[1]
	else:
		obj = {'method': t[2], value: t[3]}
		t[0] = obj

def p_b(t):
	'''b : o s
		 | '''

	if len(t) > 1:
		obj = {'operator': t[1], 'value': t[2]}
		t[0] = obj
			
def p_g(t):
	'''g : SIN LPAREN NUMBER COMA FLOAT RPAREN
		 | LIN LPAREN FLOAT COMA FLOAT RPAREN
		 | SIL paren
		 | NOI LPAREN FLOAT RPAREN
		 | FLOAT'''

	if t[1] == 'sin':
		t[0] = sin(t[3],t[5])
	elif t[1] == 'lin':
		t[0] = lin(t[3],t[5])
	elif t[1] == 'sil':
		t[0] = sil()
	elif t[1] == 'noi':
		t[0] = noi(t[3])
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
		 | POST PAREN
		 | LOOP LPAREN NUMBER RPAREN
		 | TUNE LPAREN sign NUMBER RPAREN
		 | FILL LPAREN FLOAT RPAREN
		 | REDUCE paren
		 | EXPAND paren'''

def p_sign(t):
	'''sign : POSITIVE
			| NEGATIVE
			| '''

	if t[1] == '+' or t[1] == '':
		t[0] = 1
	else:
		t[0] = -1

def p_paren(t):
	'''paren : LPAREN RPAREN
			 | '''

def p_error(t):
	print("Syntax error at '%s'" % t.value)
