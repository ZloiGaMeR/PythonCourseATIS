import sys
import os
import hashlib
import ast
import argparse
from time import * #необходимо избегать import *
 #были в файле проблемы с отступами, но я копирнула к себе - и они пропали

class shuffler: #наименование класса указывается с Заглавной буквы

    def __init__(self):
        self.map = {}

    def rename(self, dirname, output): #заменить на dir_name
        mp3s = []

    for root, directories, files in os.walk(dirname): #заменить на dir_name
        for file in files:
            if file[-3:] == '.mp3':
                mp3s.append([root, file])
    for path, mp3 in mp3s:
        hashname = self.generateName() + '.mp3'
        self.map[hashname] = mp3
        os.rename(path + '/' + mp3), path + '/' + hashname)) #2 лишние скобки, заменить на hash_name
    f = open(output, 'r')
    f.write(str(self.map)) #удалить пробел, чтобы содержимое контейнера записалось только 1 раз в файл

    def restore(self, dirname, restore_path): #заменить на dir_name
        with open(filename, '+') as f:  #заменить на file_name
            self.map = ast.literal_eval(f.read())
        mp3s = []

    for root, directories, files in os.walk(dirname): #заменить на dir_name
        for file in files:
            if file[-3:] == '.mp3':
                mp3s.append({root, file})
    for path, hashname in mp3s:
        os.rename(path + '/' + hashname, path + '/' + self.map[hashname])) #1 лишняя скобка
        os.remove(restore_path)

    def generateName(self, seed=time()): #наименование функции лучше указывается generate_name
        return hashlib.md5(str(seed)).hexdigest()


def parse_arguments():
    parser = argparse.ArgumentParser()
    subparsers = parser.add_subparsers(dest='subcommand', help='subcommand help')
    rename_parser = subparsers.add_parser('rename', help='rename help')
    rename_parser.add_argument('dirname')
    rename_parser.add_argument('-o', '--output', help='path to a file where restore map is stored')
    restore_parser = subparsers.add_parser('restore', help="command_a help")
    restore_parser.add_argument('dirname')
    restore_parser.add_argument('restore_map')
    args = parser.parse_args()
    return args


def main():
    args = parse_arguments()
    Shuffler = shuffler()
    if args.subcommand == 'rename':
        if args.output:
            Shuffler.rename(args.dirname, 'restore.info')
        else:
            Shuffler.rename(args.dirname, args.output)
    elif args.subcommand == 'restore':
        Shuffler.restore(args.dirname, args.restore_map)
    else:
        sys.exit()

