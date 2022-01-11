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
             | forexp
             | stmt stmt
    '''
    if len(p) == 2:
        p[0] = str(p[1])
    else:
        p[0] = str(p[1]) + "\n" + str(p[2])

def p_prnt(p):
    '''
        prnt : PRINT LPAREN LITSTRING RPAREN SM
             | PRINT LPAREN LITSTRING COMMA ID RPAREN SM
             | PRINT LPAREN LITSTRING COMMA expr RPAREN SM
    '''
    if len(p) == 8:
        p[0] = "printf(" + p[3] +","+ p[5]+ ");\n"
        
    else:
        p[0] = "printf(" + p[3] + ");\n"
        

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
              | LT
              | GT
    '''
    
    if len(p) == 3:
        p[0] = "=="
    else:
        p[0] = str(p[1])

def p_vardec(p):
    '''
        vardec : INT ID AS LITNUM SM
               | INT ID SM
               | DOUBLE ID AS LITNUM SM
               | DOUBLE ID SM
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
    p[0] = "-"+str(p[2])

def p_mult_div( p ) :
    '''expr : expr MUL expr
            | expr DIV expr'''
    p[0] = str(p[1]) + str(p[2]) + str(p[3])

def p_expr2NUM( p ) :
    'expr : LITNUM'
    p[0] = p[1]

def p_expr2ID(p):
    'expr : ID'
    p[0] = str(p[1])

def p_bit(p):
    '''
        expr : expr bitwise expr
             | BNOT expr
    '''
    if len(p)==4:
        p[0] = str(p[1]) + str(p[2]) + str(p[3])
    else:
        p[0] = str(p[1]) + str(p[2])

def p_bitwise(p):
    '''
        bitwise :   BAND
                |   BOR
                |   EXP
                |   BLS
                |   BRS
    '''
    p[0] = str(p[1])


def p_parens( p ) :
    'expr : LPAREN expr RPAREN'
    p[0] = str(p[1]) + str(p[2]) + str(p[3])


def p_for( p ) :
    'forexp : FOR LPAREN vardec rela SM unaryarith RPAREN LBRACE stmt RBRACE'

    p[0] = str(p[1]) + " " + str(p[2])+str(p[3])+ " " + str(p[4])+str(p[5])+ " " +str(p[6])+str(p[7])+"\n"+str(p[8])+str(p[9])+str(p[10])

def p_unaryarith( p ):
    '''
        unaryarith : ID INC
                   | ID DEC
                   | DEC ID
                   | INC ID
                   | ID AS expr
    '''

    if len(p)==3:
        p[0] = str(p[1])+str(p[2])
    else:
        p[0] = str(p[1])+str(p[2])+str(p[3])

def p_unu( p ):
    '''
        unu : AND 
            | AUTO
            | BREAK
            | CASE
            | CHAR
            | COLON
            | COMMENT
            | COND_TERN
            | CONST
            | CONTINUE
            | DEFAULT
            | DO
            | DOT
            | DOUBLE
            | END
            | EQ
            | EXTERM
            | FLOAT
            | FUNCTION
            | GOTO
            | KEY
            | LBRACKET
            | RBRACKET
            | LITCHAR
            | LONG
            | MOD
            | NOT
            | OR
            | REGISTER
            | REST
            | RETURN
            | SHORT
            | SIGNED
            | SIZEOF
            | STATIC
            | STRUCT
            | SWITCH
            | TYPEDEF
            | UNION
            | UNSIGNED
            | VARIABLE
            | VOID
            | VOLATILE
            | WHILE
            | BXOR
    '''

def p_error( p ):
    print("Syntax error in input! : ", p)
    exit()