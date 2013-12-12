from parser import * 

import ply.yacc as yacc
yacc.yacc()

while 1:
    try:
        # s = input('calc > ')   # Use raw_input on Python 2
        s = '{{-1;1}.loop(44).expand(1).tune(-1).loop(3).fill(3)}.loop(5).post()'
    except EOFError:
        break
    yacc.parse(s)
    break
