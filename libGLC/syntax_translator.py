from libGLC.io import InputFile
import ply.lex as lex
import libGLC.lang_defs.keywords as keywords

# Build the lexer
lexer = lex.lex(module=keywords)

def syntax_translate(code, lang):
    print('starting syntax translation for lang : {lang}'.format(lang = lang))

    '''
        Load the tokens regex and the CFG for this language. Use that to parse
        and translate
    '''

    print(code)

    # Give the lexer some input
    lexer.input(code)
 
    # Tokenize
    while True:
        tok = lexer.token()
        if not tok: 
            break      # No more input
        print(tok)

if __name__ == "__main__":
    inFile = InputFile("testout.glc")
    lines = inFile.file.read()

    syntax_translate(lines, 'tamil')
