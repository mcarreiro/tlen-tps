
# -----------------------------------------------------------------------------
# calc.py
#
# A simple calculator with variables -- all in one file.
# -----------------------------------------------------------------------------

tokens = (
    'CON','MIX','ADD','SUB','MUL','DIV','SIN',
    'LIN','NOI','SIL','PLAY','POST','LOOP',
	'TUNE','FILL','REDUCE','EXPAND','NUMBER','LKEY','RKEY',
	'LPAREN','RPAREN','POINT','COMA', 'FLOAT', 'PAREN','POSITIVE','NEGATIVE'
    )

# Tokens

t_CON    = r'con|;'
t_MIX   = r'mix|&'
t_ADD   = r'add|\+'
t_SUB  = r'sub|-'
t_MUL  = r'mul|\*'
t_DIV  = r'div|/'
t_SIN  = r'sin'
t_POSITIVE = r'\+'
t_NEGATIVE = r'-'

t_LIN  = r'lin|linear'
t_NOI  = r'noi|noise'
t_SIL  = r'sil|silence'
t_PLAY  = r'play'
t_POST  = r'post'
t_LOOP  = r'loop'
t_TUNE  = r'tune'
t_FILL  = r'fill'
t_REDUCE  = r'reduce'
t_EXPAND  = r'expand'
t_LPAREN  = r'\('
t_RPAREN  = r'\)'
t_LKEY  = r'\{'
t_RKEY  = r'\}'
t_POINT  = r'.'
t_COMA = r','

#t_SIGN = r'(\+|-)?'
#t_PAREN = r'(\(\))?'
#t_NAME    = r'[a-zA-Z_][a-zA-Z0-9_]*'

def t_FLOAT(t):
    r'[+-]?(\d+(\.\d*)?|\.\d+)([eE][+-]?\d+)?'
    try:
        t.value = float(t.value)
    except ValueError:
        print("Float value too large %d", t.value)
        t.value = 0
    return t

def t_NUMBER(t):
    r'\d+'
    try:
        t.value = int(t.value)
    except ValueError:
        print("Integer value too large %d", t.value)
        t.value = 0
    return t

# Ignored characters
t_ignore = " \t"

def t_newline(t):
    r'\n+'
    t.lexer.lineno += t.value.count("\n")
    
def t_error(t):
    print("Illegal character '%s'" % t.value[0])
    t.lexer.skip(1)
    
# Build the lexer
import ply.lex as lex
lex.lex()

#precedence = (
#    ('left','PLUS','MINUS'),
#    ('left','TIMES','DIVIDE'),
#    ('right','UMINUS'),
#    )

# dictionary of names
#names = { }

def p_s(t):
    '''s : LKEY s RKEY a
				 | g b'''

def p_a(t):
    '''a : POINT p a 
		 | b'''
    if t[1] != '.':
        t[0] = t[1]

def p_b(t):
	'''b : o s
		 | '''
	if t[1] == ';' or t[1] == 'con':
        t[0] = t[0] + t[2]
	else:
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
            
def p_g(t):
	'''g : SIN LPAREN NUMBER COMA FLOAT RPAREN
		 | LIN LPAREN FLOAT COMA FLOAT RPAREN
		 | SIL paren
		 | NOI LPAREN FLOAT RPAREN
		 | FLOAT'''
#		 | SIN LPAREN NUMBER RPAREN
#	 	 | NOISE
    if t[1] == 'sin':
    elif t[1] == 'lin':
    elif t[1] == 'sil':
    elif t[1] == 'noi':
    else
        t[0][0] = t[1]

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
	''' sign : POSITIVE
			 | NEGATIVE
			 | '''

def p_paren(t):
	''' paren : LPAREN RPAREN
			 | '''

def p_error(t):
    print("Syntax error at '%s'" % t.value)

import ply.yacc as yacc
yacc.yacc()

while 1:
    try:
        s = input('calc > ')   # Use raw_input on Python 2
    except EOFError:
        break
    yacc.parse(s)
