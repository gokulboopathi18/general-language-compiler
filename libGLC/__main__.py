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
from libGLC.utils import stringsplit

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

# code is an array of lines
# ignore lines that start with a #


def translate(code, map):
    print('starting lexical translation')

    total_code = ""

    for line in code:
        # this splits based on white space, if there is no whte space it can't figure out the word
        values = stringsplit(line)
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

    return total_code


def symbol_extraction(code):
    # data = file.read()
    print("Doint symbol extraction")
    arr = {}
    flag = 0
    ind = 0
    count = 0

    lines = code.split("\n")
    # print(lines)
    for each_line in lines:
        # print(each_line)
        #words = each_line.split()
        words = stringsplit(each_line)
        inside_string = 0

        for i in range(len(words)):
            word = words[i]
            inside_string = inside_string + word.count('\"')
            # print(word)

            if inside_string % 2 == 0:
                if len(word)>=1 and ord(word[0]) > 256:
                    for j in range(len(word)):
                        if word[j] != ';':
                            continue
                        else:
                            flag = 1
                            break
                    if flag == 0:
                        for x in range(ind):
                            if word in arr.keys():
                                count += 1
                        if(count == 0):
                            arr[word] = "t"+str(ind)
                            ind += 1
                        else:
                            count = 0

                    else:
                        for x in range(ind):
                            if word in arr.keys():
                                count += 1
                        if(count == 0):
                            arr[word[0:j]] = "t"+str(ind)
                            ind += 1
                        else:
                            count = 0
                        flag = 0
                else:
                    continue
            else:
                continue

    print("Symbols = ", arr)
    return arr


def symbol_translation(code, map):
    output_code = ""
    print("<< doing symbol translation >>")

    lines = code.split("\n")
    for each_line in lines:
        #words = each_line.split()
        words = stringsplit(each_line)
        for word in words:
            if map.__contains__(word):
                output_code += map[word]
            else:
                output_code += word
            output_code += " "
        output_code += "\n"

    return output_code


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
    print('language: \"{lang}\"'.format(lang=lang))

    # get translation map
    try:
        trans_map = translation[lang]
        print('found translation map')
    except:
        raise InvalidLanguage(
            'the language \"${lang}\" is invalid or unsupported'.format(lang=lang))

    print()

    # translate
    INTERMEDIATE = translate(SOURCE_CODE, trans_map)

    new_variables = symbol_extraction(INTERMEDIATE)
    OUTPUT = symbol_translation(INTERMEDIATE, new_variables)
    output_file = open("out.glc", "w")
    output_file.write(OUTPUT)


if __name__ == "__main__":
    main()
