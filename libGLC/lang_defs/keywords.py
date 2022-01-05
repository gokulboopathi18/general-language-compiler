'''
    These are the tokens for every language. 
    This is because we convert everything to this 
    standard set of tokens
'''

reserved = {
    "auto" : "AUTO",
    "break" :"BREAK",
    "case" : "CASE",
    "char" : "CHAR",
    "const" : "CONST",
    "continue" : "CONTINUE",
    "default" : "DEFAULT",
    "do" : "DO",
    "double" : "DOUBLE",
    "else" : "ELSE",
    "end" : "END",
    "enum" : "ENUM",
    "extern" : "EXTERM",
    "float" : "FLOAT",
    "for" : "FOR",
    "function" : "FUNCTION",
    "goto" : "GOTO",
    "if" : "IF",
    "int" : "INT",
    "long" : "LONG",
    "print" : "PRINT",
    "register" : "REGISTER",
    "return" : "RETURN",
    "short" : "SHORT",
    "signed" : "SIGNED",
    "sizeof" : "SIZEOF",
    "static" : "STATIC",
    "struct" : "STRUCT",
    "switch" :"SWITCH",
    "typedef" : "TYPEDEF",
    "union" : "UNION",
    "unsigned" : "UNSIGNED",
    "variable" : "VARIABLE",
    "void" : "VOID",
    "volatile" : "VOLATILE",
    "while": "WHILE" 
}

tokens = [
    'PLUS',
    'MINUS', 
    'DIV', 
    'MUL', 
    'MOD', 
    'EXP', 
    'INC', 
    'DEC',
    'GT',
    'LT',
    'EQ',
    'NEQ',
    'GTE',
    'AS',
    'LTE',
    'BAND',
    'BOR',
    'BNOT',
    'BXOR',
    'BLS',
    'BRS',
    'AND',
    'OR',
    'NOT',
    'COND_TERN',
    'ID',
    'DOT',
    'COMMA',
    'SM',
    'COLON',
    'LPAREN',
    'RPAREN',
    'LBRACE',
    'RBRACE',
    'LBRACKET',
    'RBRACKET',
    'LITNUM',
    'LITCHAR',
    'LITSTRING', 
    'COMMENT',
    'KEY',
    'REST'

] + list(reserved.values())


'''
    REGEX RULES FOR TOKENS
'''

# operators : arithmetic
t_PLUS = r'\+'
t_MINUS = r'-'
t_MUL = r'\*'
t_DIV = r'/'
t_MOD = r'%'    # todo: check if op
t_EXP = r'\^'
t_INC = r'\+\+'
t_DEC = r'\-\-'

# operators : relational
t_GT = r'>'
t_LT = r'<'
t_EQ = r'=='
t_NEQ = r'!='
t_GTE = r'>='
t_LTE = r'<='

# operators : bitwise
t_BAND = r'&'
t_BOR = r'\|'
t_BNOT = r'~'
t_BXOR = r'\$'   # todo: what about caret?
t_BLS = r'<<'
t_BRS = r'>>'

# operators : logical
t_AND = r'&&'
t_OR = r'\|\|'
t_NOT = r'!'

t_AS = r'\='

# operators : ternary
t_COND_TERN = r'\?'

# separators
t_DOT = r'\.'
t_COMMA = r','
t_SM = r'\;'
t_COLON = r':'

t_LPAREN  = r'\('
t_RPAREN  = r'\)'

t_LBRACE  = r'{'
t_RBRACE  = r'}'

t_LBRACKET  = r'\['
t_RBRACKET  = r'\]'

# literals
'LITNUM', 'LITCHAR', 'LITSTRING' 
# literals
def t_LITNUM(t):
    r'[\+\-]?\d+'
    t.value = int(t.value)    
    return t

def t_LITCHAR(t):
    r'\'.\''
    t.value = str(t.value)    
    return t

def t_LITSTRING(t):
    r'\".*\"'
    t.value = str(t.value)    
    return t

# identifier
def t_ID(t):
    r'id[0-9]+'
    t.type = reserved.get(t.value,'ID')    # Check for reserved words
    return t

def t_KEY(t):
    r'[a-zA-Z_][a-zA-Z_0-9]*'
    t.type = reserved.get(t.value)
    return t

# ignore comments
def t_COMMENT(t):
    r'\#.*'
    pass

# to track line numbers
def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)

# ignore spaces and tabs
t_ignore  = ' \t'
# t_REST = r'.+'

# Error handling rule
def t_error(t):
    print("Illegal character '%s'" % t.value[0])
    print(t.lexer.lineno)
    exit()

