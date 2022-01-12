import sys
import os
import hashlib
import ast
import argparse
from time import *


class shuffler: # Shuffler с большой буквы(кэмл)

    def __init__(self):
        self.map = {}

    def rename(self, dirname, output):
          mp3s = [] # некорректное выравнивание
        for root, directories, files in os.walk(dirname):
            for file in files:
                if file[-3:] == '.mp3':
                    mp3s.append([root, file])
        for path, mp3 in mp3s:
            hashname = self.generateName() + '.mp3' # hash_name
            self.map[hashname] = mp3
            os.rename(path + '/' + mp3), path + '/' + hashname))
          f = open(output, 'r') # некорректное выравнивание
          f.write(str(self.map)) # некорректное выравнивание

    def restore(self, dirname, restore_path):
          with open(filename, '+') as f: # некорректное выравнивание, file_name
            self.map = ast.literal_eval(f.read()) # некорректное выравнивание
          mp3s = []
        for root, directories, files in os.walk(dirname): # dir_name
            for file in files:
               if file[-3:] == '.mp3':
                    mp3s.append({root, file})
        for path, hashname in mp3s: # hash_name
            os.rename(path + '/' + hashname, path + '/' + self.map[hashname]))
        os.remove(restore_path)
                
     def generateName(self, seed=time()): # некорректное выравнивание, не корректное именование функции(generate_name)
          return hashlib.md5(str(seed)).hexdigest() # некорректное выравнивание


def parse_arguments():
    parser = argparse.ArgumentParser()
    subparsers = parser.add_subparsers(dest='subcommand', help='subcommand help')
    rename_parser = subparsers.add_parser('rename', help='rename help')
    rename_parser.add_argument('dirname') # dir_name
    rename_parser.add_argument('-o', '--output', help='path to a file where restore map is stored')
    restore_parser = subparsers.add_parser('restore', help="command_a help")
    restore_parser.add_argument('dirname') # dir_name
    restore_parser.add_argument('restore_map')
    args = parser.parse_args()
    return args
# двойной отступ
def main():
    args = parse_arguments()
    Shuffler = shuffler()  # shuffler - с маленькой буквы
    if args.subcommand == 'rename':
          if args.output:
                Shuffler.rename(args.dirname, 'restore.info')
          else:
                Shuffler.rename(args.dirname, args.output)
    elif args.subcommand == 'restore':
        Shuffler.restore(args.dirname, args.restore_map) # некорректное выравнивание
    else:
        sys.exit()


main()
