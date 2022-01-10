'''
    Converts code to an intermediate english-text
    representation
'''
import subprocess

from libGLC.consts import IN_FILE
from libGLC.lang_defs.sanskrit.lex_map import definitions as sanskrit_translation
from libGLC.lang_defs.tamil.lex_map import definitions as tamil_translation
from libGLC.io import CmdArgs, InputFile
from libGLC.errors import *
from libGLC.consts import *
from libGLC.shared import SOURCE_CODE
from libGLC.syntax_translator import syntax_translate
from libGLC.utils import stringsplit, writeArray


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
    total_code = []

    for line in code:
        # this splits based on white space, if there is no whte space it can't figure out the word
        values = stringsplit(line)
        length = len(values)
        # print(values)

        i = 0
        cur_line = []
        inside_string = 0
        comm = False
        while i < length:
            two = False
            inside_string = inside_string + values[i].count('\"')   #avoids converting character if it is inside a string
            if values[i] == "#":
                comm = True
            if comm == False and inside_string % 2 == 0 :
                if map.__contains__(values[i]):
                    cur_line.append(map[values[i]])

                # checking if the current and next word together forms a keyword
                elif i+2 < length and map.__contains__(values[i]+" "+values[i+2]):
                    two = True
                    cur_line.append(map[values[i]+" "+values[i+2]])
                else:
                    cur_line.append(values[i])
            else:
                cur_line.append(values[i])

            if two:
                i += 3
            else:
                i += 1

        total_code.append(cur_line)

    print('lexical translation complete\n')
    return total_code


def symbol_extraction(code):
    arr = {}
    flag = 0
    ind = 0
    count = 0


    for each_line in code:

        words = each_line
        inside_string = 0

        for i in range(len(words)):
            word = words[i]
            inside_string = inside_string + word.count('\"')
            if word == "#":
                break

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
                            arr[word] = "id"+str(ind)
                            ind += 1
                        else:
                            count = 0

                    else:
                        for x in range(ind):
                            if word in arr.keys():
                                count += 1
                        if(count == 0):
                            arr[word[0:j]] = "id"+str(ind)
                            ind += 1
                        else:
                            count = 0
                        flag = 0
                else:
                    continue
            else:
                continue

    print(">> Symbols with their changed english variable names\n")

    print(">>\tSymbol\t\tVariable")
    print("======================================")
    for key in arr:
        print(">>\t", key, "\t\t", arr[key])

    return arr


def symbol_translation(code, map):
    i = 0
    for each_line in code:
        j = 0
        inside_string = 0
        # comm = False

        for word in each_line:
            inside_string = inside_string + word.count('\"')
            if word == "#":
                break
            if inside_string%2==0 and map.__contains__(word):
                code[i][j] = map[word]
            j+=1     
        i+=1



    return code

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
    print("<< Starting Language translation >>")
    INTERMEDIATE = translate(SOURCE_CODE, trans_map)
    inter_output = open("out.language.glc", "w")
    print("<< language translation done, saved in \'out.language.glc\'")
    OUTPUT_STR = writeArray(INTERMEDIATE)
    inter_output.write(writeArray(INTERMEDIATE))

    print()
    print("<< Starting symbol extraction >>")
    new_variables = symbol_extraction(INTERMEDIATE)

    print()
    print("<< Doing symbol translation >>")
    OUTPUT = symbol_translation(INTERMEDIATE, new_variables)

    print("<< symbol translation done, saved in \'out.symbol.glc\'")

    output_file = open("out.symbol.glc", "w")
    OUTPUT_STR = writeArray(OUTPUT)
    output_file.write(OUTPUT_STR)

    IND = syntax_translate(OUTPUT_STR, lang)

    print("\n>> Syntax translation done and saved in \'c_out.c\'")
    
    final_out = open("c_out.c", 'w')
    final_out.write(IND)
    final_out.close()

    print("\n>> $gcc c_out.c")
    tmp = subprocess.call("gcc c_out.c;", shell=True)
    
    # subprocess.call(["g", "c_out.c", "-o", "output", "-std=c99", '-w', '-Ofast']) 
    print("\n>> ./a.out")
    print()
    tmp = subprocess.call("./a.out", shell=True)
    print()


if __name__ == "__main__":
    main()
