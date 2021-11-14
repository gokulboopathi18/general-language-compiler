import argparse
from os.path import isfile
from libGLC.consts import *

class InputFile():
    def __init__(self, filepath):
        if not isfile(filepath):
            raise FileNotFoundError("\"{filename}\" doesn't exist".format(filename=filepath))
        

        self.filepath = filepath
        self.file = open(filepath, 'r')


    def close(self):
        self.file.close()
        self.file = None

    def read(self):
        return self.file.read()



class CmdArgs():
    def __init__(self):
        self.parser = argparse.ArgumentParser(description="General Language Compiler, commmand line arguments")

        self.parser.add_argument(
            '-if',
            '--inputFile',
            type=str,
            help="The path to the file containing the source code",
            dest=IN_FILE,
            required=True
        )

        self.args = self.parser.parse_args()

    def getArg(self, argName):
        return vars(self.args)[argName]