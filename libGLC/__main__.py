'''
    Converts code to an intermediate english-text
    representation
'''

from libGLC.consts import IN_FILE
from libGLC.lang_defs.sanskrit.lex_map import definitions as sanskrit_translation
from libGLC.lang_defs.tamil.lex_map import definitions as tamil_translation
from libGLC.io import CmdArgs, InputFile
from libGLC.errors import *
from libGLC.consts import *
from libGLC.shared import SOURCE_CODE
from libGLC.syntax_translator import syntax_translate

translation = {
    "tamil": tamil_translation,
    "sanskrit": sanskrit_translation
}


def get_language(lines):
    print('identifying language : looking for shebang')
    for line in lines:
        text = line.strip()
        if(text):
            if(text.startswith(SHEBANG)):
                return text.lstrip(SHEBANG)
            else:
                return None
    return None


'''
    Lexical translation
'''
def translate(code, map):
    print('starting lexical translation')

    total_code = ""

    for line in code:
        # this splits based on white space, if there is no whte space it can't figure out the word
        values = line.split()
        length = len(values)
        # print(values)

        i = 0
        str = ""
        inside_string = 0
        while i < length:
            two = False
            inside_string = inside_string + values[i].count('\"')
            if inside_string % 2 == 0:
                if map.__contains__(values[i]):
                    str += map[values[i]]

                # checking if the current and next word together forms a keyword
                # todo, check for some better implementation
                elif i+1 < length and map.__contains__(values[i]+" "+values[i+1]):
                    two = True
                    str += map[values[i]+" "+values[i+1]]
                else:
                    str += values[i]
            else:
                str += values[i]

            if two:
                i += 2
            else:
                i += 1
            if i < length:
                str += " "

            # todo: once the better impementation is done
                # todo: collect identifiers, build symbol table

        # print(str)
        total_code += str+"\n"

    print('lexical translation complete\n')
    return total_code

def main():
    print('general-language-compiler v1.0.0')

    # parse command line args
    args = CmdArgs()
    inFileName = args.getArg(IN_FILE)

    # get source code
    inFile = InputFile(inFileName)
    lines = inFile.file.readlines()

    SOURCE_CODE = lines

    # recognize language
    print()
    lang = get_language(SOURCE_CODE)
    if(not lang):
        raise MissingLanguageDeclaration(
            'language declaration statement not found in the beginning of the source code')
    print('language: \"{lang}\"\n'.format(lang=lang))

    # get translation map
    try:
        trans_map = translation[lang]
        print('found translation map')
    except:
        raise InvalidLanguage(
            'the language \"${lang}\" is invalid or unsupported'.format(lang=lang))

    print()

    # translate
    OUTPUT = translate(SOURCE_CODE, trans_map)
    output_file = open("out.glc", "w")
    output_file.write(OUTPUT)


    IND = syntax_translate(OUTPUT, lang)



if __name__ == "__main__":
    main()
