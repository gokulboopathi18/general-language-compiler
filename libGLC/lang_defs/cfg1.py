from libGLC.lang_defs.keywords import tokens

precedence = (
    ( 'left', 'PLUS', 'MINUS' ),
    ( 'left', 'MUL', 'DIV' ),
    ( 'nonassoc', 'UMINUS' )
)

def p_stmt(p):
    '''
        stmt : vardec
             | cond
             | as
             | prnt
             | stmt stmt
    '''
    if len(p) == 2:
        p[0] = str(p[1])
    else:
        p[0] = str(p[1]) + "\n" + str(p[2])

def p_prnt(p):
    '''
        prnt : PRINT LPAREN LITSTRING RPAREN SM
    '''
    p[0] = "printf(" + p[3] + ")\n"

def p_cond(p):
    '''
        cond : LPAREN rela RPAREN IF LBRACE stmt RBRACE
             | LPAREN rela RPAREN IF LBRACE stmt RBRACE ELSE LBRACE stmt RBRACE
    '''

    if len(p) == 7:
        p[0] = str(p[4]) + str(p[1]) + str(p[2]) + str(p[3]) + " " + str(p[5])+ "\n\t" +  str(p[6]) + "\n" + str(p[7])
    else:
        p[0] = str(p[4]) + str(p[1]) + str(p[2]) + str(p[3]) + " " + str(p[5])+ "\n\t" +  str(p[6]) + "\n" + str(p[7]) + " else{\n\t" +  str(p[10]) + "}\n"
    
def p_as(p):
    '''
        as : ID AS expr SM
    '''
    p[0] = str(p[1]) + " " + str(p[2]) + " " + str(p[3]) + str(p[4]) + "\n"

def p_rela(p):
    '''
        rela : ID relop expr
             | expr relop ID
    '''
    p[0] = str(p[1]) + str(p[2]) + str(p[3])

def p_relop(p):
    '''
        relop : AS AS 
              | NEQ
              | GTE
              | AS
              | LTE
    '''
    
    if len(p) == 3:
        p[0] = "=="
    else:
        p[0] = str(p[1])

def p_vardec(p):
    '''
        vardec : INT ID AS LITNUM SM
               | INT ID SM
    '''
    if len(p) == 6:
        p[0] = str(p[1]) + " " + str(p[2]) + " " +  str(p[3]) + " " +  str(p[4]) + str(p[5])
    else:
        p[0] = str(p[1]) + " " +  str(p[2]) + str(p[3])

def p_add( p ) :
    'expr : expr PLUS expr'
    p[0] = str(p[1]) + '+' + str(p[3])

def p_sub( p ) :
    'expr : expr MINUS expr'
    p[0] = str(p[1]) + '-' + str(p[3])

def p_expr2uminus( p ) :
    'expr : MINUS expr %prec UMINUS'

def p_mult_div( p ) :
    '''expr : expr MUL expr
            | expr DIV expr'''
    p[0] = str(p[1]) + str(p[2]) + str(p[3])

def p_expr2NUM( p ) :
    'expr : LITNUM'
    p[0] = p[1]

def p_parens( p ) :
    'expr : LPAREN expr RPAREN'
    p[0] = str(p[1]) + str(p[2]) + str(p[3])

def p_error( p ):
    print("Syntax error in input!")