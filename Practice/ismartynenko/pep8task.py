import sys
import os
import hashlib
import ast
import argparse
from time import *


class Shuffler:                                            # Camel Case

    def __init__(self):
        self.map = {}

    def rename(self, dirname, output):
        mp3s = []                                           # было 6 пробелов, а не 4
                                                            # не было пустой строки
    for root, directories, files in os.walk(dirname):       # уменьшил отступ
        for file in files:                                  # уменьшил отступ
            if file[-3:] == '.mp3':                         # уменьшил отступ
                mp3s.append([root, file])                   # уменьшил отступ
                                                            # не было пустой строки
        for path, mp3 in mp3s:
            hashname = self.generateName() + '.mp3'
            self.map[hashname] = mp3
            os.rename(path + '/' + mp3, path + '/' + hashname)    # похоже на 2 лишние ')'
            f = open(output, 'r')                           # было 2 лишних пробела
            f.write(str(self.map))                          # было 2 лишних пробела

    def restore(self, dirname, restore_path):
        with open(filename, '+') as f:                      # было 6 пробелов, а не 4
            self.map = ast.literal_eval(f.read())
            mp3s = []                                       # add 2 spaces
                                                            # add empty string
        for root, directories, files in os.walk(dirname):
            for file in files:
                if file[-3:] == '.mp3':                     # add 1 space
                    mp3s.append({root, file})
                                                            # add empty string
        for path, hashname in mp3s:
            os.rename(path + '/' + hashname, path + '/' + self.map[hashname])  # extra ')'
            os.remove(restore_path)                         # add 4 spaces
                
    def generatename(self, seed=time()):                    # delete 1 space and lowercase
        return hashlib.md5(str(seed)).hexdigest()           # delete 2 spaces


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


def main():                                                 # add empty string
    args = parse_arguments()
    shuffler = Shuffler()
    if args.subcommand == 'rename':
        if args.output:                                     # delete 2 spaces
            Shuffler.rename(args.dirname, 'restore.info')   # delete 4 spaces
        else:                                               # delete 2 spaces
            Shuffler.rename(args.dirname, args.output)      # delete 4 spaces
    elif args.subcommand == 'restore':
        Shuffler.restore(args.dirname, args.restore_map)
    else:
        sys.exit()


main()
