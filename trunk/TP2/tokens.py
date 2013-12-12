tokens = (
    'CON','MIX','ADD','SUB','MUL','DIV','SIN',
    'LIN','NOI','SIL','PLAY','POST','LOOP',
	'TUNE','FILL','REDUCE','EXPAND','NUMBER','LKEY','RKEY',
	'LPAREN','RPAREN','POINT','COMA', 'FLOAT'#,'POSITIVE','NEGATIVE'
    )

# Tokens

t_CON    = r'con|;'
t_MIX   = r'mix|&'
t_ADD   = r'add|\+'
t_SUB  = r'sub|-'
t_MUL  = r'mul|\*'
t_DIV  = r'div|/'
t_SIN  = r'sin'
# t_POSITIVE = r'\+'
# t_NEGATIVE = r'-'

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
    r'[-+]?\d+\.\d+'
    try:
        t.value = float(t.value)
    except ValueError:
        print("Float value too large %d", t.value)
        t.value = 0
    return t

def t_NUMBER(t):
    r'[-+]?\d+'
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