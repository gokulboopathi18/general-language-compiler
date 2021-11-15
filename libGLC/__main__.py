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
    "tamil": tamil_translation,
    "sanskrit": sanskrit_translation
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

# code is an array of lines
# ignore lines that start with a #


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
        while i < length:
            two = False
            if map.__contains__(values[i]):
                str += map[values[i]]

            # checking if the current and next word together forms a keyword
            # todo, check for some better implementation
            elif i+1 < length and map.__contains__(values[i]+" "+values[i+1]):
                two = True
                str += map[values[i]+" "+values[i+1]]
            else:
                str += values[i]

            if two:
                i += 2
            else:
                i += 1
            if i < length:
                str += " "

        # print(str)
        total_code += str+"\n"

    return total_code

    # todo for every word in the code that matches something in the map, make the change and store the changed version in


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
        raise MissingLanguageDeclaration(
            'language declaration statement not found in the beginning of the source code')
    print('language: \"{lang}\"'.format(lang=lang))

    try:
        trans_map = translation[lang]
    except:
        raise InvalidLanguage(
            'the language \"${lang}\" is invalid or unsupported'.format(lang=lang))

    print()
    SOURCE_CODE = lines
    # print(SOURCE_CODE)
    OUTPUT = translate(SOURCE_CODE, trans_map)
    print(OUTPUT)
    output_file = open("out.glc", "w")
    output_file.write(OUTPUT)


if __name__ == "__main__":
    main()
