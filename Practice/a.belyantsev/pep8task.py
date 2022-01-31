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
          mp3s = [] # сдвиг в лево 2 пробела
        for root, directories, files in os.walk(dirname):
            for file in files:
                if file[-3:] == '.mp3':
                    mp3s.append([root, file])
        for path, mp3 in mp3s:
            hashname = self.generateName() + '.mp3' # hash_name
            self.map[hashname] = mp3
            os.rename(path + '/' + mp3), path + '/' + hashname)) #лишние скобки после "mp3" и последняя
          f = open(output, 'r') # сдвиг влево 2 проблеа
          f.write(str(self.map)) # сдвиг влево 2 проблеа, файл открыт на чтение а производим запись

    def restore(self, dirname, restore_path):  #dir_name
          with open(filename, '+') as f: # сдвиг влево на 2, filename - не существует в области функции restore.
                                         # Ключ режима открытия файла "+" используется только в сочетании с r или w
            self.map = ast.literal_eval(f.read())
          mp3s = [] #  сдвиг влево на 2
        for root, directories, files in os.walk(dirname): # dir_name
            for file in files:
               if file[-3:] == '.mp3':
                    mp3s.append({root, file})
        for path, hashname in mp3s: # hash_name
            os.rename(path + '/' + hashname, path + '/' + self.map[hashname])) # последняя скобка лишняя
        os.remove(restore_path)
                
     def generateName(self, seed=time()): # сдвиг влево на 1, не корректное именование функции(generate_name)
          return hashlib.md5(str(seed)).hexdigest() # сдвиг влево на 1


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
          if args.output: # сдвиг влево на 1
                Shuffler.rename(args.dirname, 'restore.info') # сдвиг влево на 1
          else: # сдвиг влево на 1
                Shuffler.rename(args.dirname, args.output) # сдвиг влево на 1
    elif args.subcommand == 'restore':
        Shuffler.restore(args.dirname, args.restore_map)
    else:
        sys.exit()


main()
