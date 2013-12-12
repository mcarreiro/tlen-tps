from parser import * 

import ply.yacc as yacc
yacc.yacc()

while 1:
    try:
        # s = input('calc > ')   # Use raw_input on Python 2
        s = '{3}.post'
    except EOFError:
        break
    yacc.parse(s)
    break
