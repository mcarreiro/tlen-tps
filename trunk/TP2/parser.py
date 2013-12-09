from tokens import *

def p_s(t):
	'''s : LKEY s RKEY a
		 | g b'''

	if 1 in t and 2 in t and t[1] != '{':		
		t[0] = t[1]+t[2]
	else:
		pass

	print t[0]

def p_a(t):
	'''a : POINT p a 
		 | b'''
	if t[1] != '.':
		t[0] = t[1]

def p_b(t):
	'''b : o s
		 | '''

	if 1 in t and (t[1] == ';' or t[1] == 'con'):		
		t[0] = t[0] + t[2]
		print t[0]
	elif 1 in t and (t[1] != ';' and t[1] != 'con'):
		x = len(t[0])
		y = len(t[2])
		i = 0
		res = []        
		while i < x or i < y:
			if t[1] == '+' or t[1] == 'add':
				res[i] = t[0][i%x] + t[2][i%y]
			elif t[1] == '-' or t[1] == 'sub':
				res[i] = t[0][i%x] - t[2][i%y]
			elif t[1] == '*' or t[1] == 'mul':
				res[i] = t[0][i%x] * t[2][i%y]
			elif t[1] == '/' or t[1] == 'div':
				res[i] = t[0][i%x] / t[2][i%y]
			elif t[1] == '&' or t[1] == 'mix':
				res[i] = (t[0][i%x] + t[2][i%y])/2     
			i = i + 1
		t[0] = res
	else:
		t[0] = []
			
def p_g(t):
	'''g : SIN LPAREN NUMBER COMA FLOAT RPAREN
		 | LIN LPAREN FLOAT COMA FLOAT RPAREN
		 | SIL paren
		 | NOI LPAREN FLOAT RPAREN
		 | FLOAT'''

	if t[1] == 'sin':
		pass
	elif t[1] == 'lin':
		pass
	elif t[1] == 'sil':
		pass
	elif t[1] == 'noi':
		pass
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

	# if t[1] == '+' or t[1] == '':
	# 	t[0] = 1
	# else:
	# 	t[0] = -1

def p_paren(t):
	'''paren : LPAREN RPAREN
			 | '''

def p_error(t):
	print("Syntax error at '%s'" % t.value)
