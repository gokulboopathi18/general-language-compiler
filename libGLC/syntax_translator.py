from libGLC.io import InputFile
import ply.lex as lex
import ply.yacc as yacc
import libGLC.lang_defs.keywords as keywords
import libGLC.lang_defs.cfg1 as cfg1

# Build the lexer
lexer = lex.lex(module=keywords)
parser = yacc.yacc(module=cfg1)

def syntax_translate(code, lang):
    print('starting syntax translation for lang : {lang}'.format(lang = lang))

    '''
        Load the tokens regex and the CFG for this language. Use that to parse
        and translate
    '''

    # parse
    res = '''
#include<stdio.h>
#include<stdlib.h>
#include<strings.h>

int main () {
'''

    res += parser.parse(code)
    res += '''
return 0;
}
'''

    lexer.input(code)
    # Tokenize
    while True:
        tok = lexer.token()
        if not tok: 
            break      # No more input
        # print(tok)
        
    return res

if __name__ == "__main__":
    inFile = InputFile("testout.glc")
    lines = inFile.file.read()

    syntax_translate(lines, 'tamil')
