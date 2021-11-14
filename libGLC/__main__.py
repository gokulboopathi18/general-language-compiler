'''
    Converts code to an intermediate english-text
    representation
'''

from libGLC.consts import IN_FILE
from libGLC.defs.sanskrit_def import definitions as sanskrit_translation
from libGLC.defs.tamil_def import definitions as tamil_translation
from libGLC.io import CmdArgs, InputFile
from libGLC.errors import *
from libGLC.consts import *
from libGLC.shared import SOURCE_CODE

translation = {
    "tamil" : tamil_translation,
    "sanskrit" : sanskrit_translation
}


def which(lines):
    print('identifying language : looking for shebang')
    for line in lines:
        text = line.strip()
        if(text):
            if(text.startswith(SHEBANG)):
                return text.lstrip(SHEBANG)
            else:
                return None
    return None

def translate(code, map):
    print('starting lexical translation')

def main():
    print('general-language-compiler v1.0.0')

    # parse command line args
    args = CmdArgs()
    inFileName = args.getArg(IN_FILE)

    # get source code
    inFile = InputFile(inFileName)
    lines = inFile.file.readlines()

    # recognize language
    print()
    lang = which(lines)
    if(not lang):
        raise MissingLanguageDeclaration('language declaration statement not found in the beginning of the source code')
    print('language: \"{lang}\"'.format(lang=lang))

    try:
        trans_map = translation[lang]
    except:
        raise InvalidLanguage('the language \"${lang}\" is invalid or unsupported'.format(lang = lang))

    print()
    translate(SOURCE_CODE, trans_map)


if __name__ == "__main__":
    main()