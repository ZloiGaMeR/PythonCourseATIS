import sys
import os
import hashlib
# from time import *
import time # импорт в предпочтительном формате
import ast
import argparse


class Shuffler:

    def __init__(self):
        self._map = {} # сделал переменную защищенной

    def rename(self, dir_name, output):
        mp3s = []
        for root, directories, files in os.walk(dir_name):
            for file in files:
                if file[-3:] == '.mp3':
                    mp3s.append([root, file])
        for path, mp3 in mp3s:
            hash_name = self.generate_name() + '.mp3'
            self._map[hash_name] = mp3  # сделал переменную защищенной
            os.rename(path + '/' + mp3, path + '/' + hash_name)
        f = open(output, 'r')
        f.write(str(self._map))  # сделал переменную защищенной
        return None # добавил в явной форме

    def restore(self, dir_name, restore_path):
        with open(filename, '+') as f:
            self._map = ast.literal_eval(f.read())  # сделал переменную защищенной
        mp3s = []
        for root, directories, files in os.walk(dir_name):
            for file in files:
                if file[-3:] == '.mp3':
                    mp3s.append({root, file})
        for path, hash_name in mp3s:
            os.rename(path + '/' + hash_name, path + '/' + self._map[hash_name]) # сделал переменную защищенной
        os.remove(restore_path)
        return None  # добавил в явной форме

    def generate_name(self, seed=time()):
        return hashlib.md5(str(seed)).hexdigest()


def parse_arguments():
    parser = argparse.ArgumentParser()
    subparsers = parser.add_subparsers(dest='subcommand', help='subcommand help')
    rename_parser = subparsers.add_parser('rename', help='rename help')
    rename_parser.add_argument('dir_name')
    rename_parser.add_argument('-o', '--output', help='path to a file where restore map is stored')
    restore_parser = subparsers.add_parser('restore', help="command_a help")
    restore_parser.add_argument('dir_name')
    restore_parser.add_argument('restore_map')
    args = parser.parse_args()
    return args


def main():
    args = parse_arguments()
    shuffler = Shuffler()
    if args.subcommand == 'rename':
        if args.output:
            shuffler.rename(args.dir_name, 'restore.info')
        else:
            shuffler.rename(args.dir_name, args.output)
    elif args.subcommand == 'restore':
        shuffler.restore(args.dir_name, args.restore_map)
    else:
        sys.exit()


if __name__ == '__main__':
    main() # убрал под if __name__ == '__main__':
