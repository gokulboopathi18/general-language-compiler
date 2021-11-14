'''
    Converts code to an intermediate english-text
    representation
'''

from libGLC.consts import IN_FILE
from libGLC.defs.sanskrit_def import definitions as sanskrit_translation
from libGLC.defs.tamil_def import definitions as tamil_translation
from libGLC.io import CmdArgs, InputFile
from libGLC.shared import SOURCE_CODE

translation = {
    "tamil" : tamil_translation,
    "sanskrit" : sanskrit_translation
}

def main():
    print('general-language-compiler v1.0.0')

    # parse command line args
    args = CmdArgs()
    inFileName = args.getArg(IN_FILE)

    # get source code
    inFile = InputFile(inFileName)
    SOURCE_CODE = inFile.read()
    print(SOURCE_CODE)


if __name__ == "__main__":
    main()