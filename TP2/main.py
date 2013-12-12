from parser import * 

import ply.yacc as yacc
yacc.yacc()

while 1:
    try:
        # s = input('calc > ')   # Use raw_input on Python 2
        s = '3.2.loop(1.0)'
    except EOFError:
        break
    yacc.parse(s)
    break
