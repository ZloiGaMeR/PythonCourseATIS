import sys
import os
import hashlib
import ast
import argparse
import time


class Shuffler:
    def __init__(self):
        self._map = {}

    def rename(self, dir_name, output):
        mp3s = []
        for root, directories, files in os.walk(dir_name):
            for file in files:
                if file[-3:] == '.mp3':
                    mp3s.append([root, file])
        for path, mp3 in mp3s:
            hash_name = self.generatename() + '.mp3'
            self._map[hash_name] = mp3
            os.rename(path + '/' + mp3, path + '/' + hash_name)
        with open(output, 'w') as f:
            f.write(str(self._map))

    def restore(self, dir_name, restore_path):
        with open(dir_name, 'r+') as f:
            self._map = ast.literal_eval(f.read())
        mp3s = []
        for root, directories, files in os.walk(dir_name):
            for file in files:
                if file[-3:] == '.mp3':
                    mp3s.append({root, file})
        for path, hash_name in mp3s:
            os.rename(path + '/' + hash_name, path + '/' + self._map[hash_name])
        os.remove(restore_path)

    def generatename(self, seed=time.time()):
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
            shuffler.rename(args.dirname, 'restore.info')
        else:
            shuffler.rename(args.dirname, args.output)
    elif args.subcommand == 'restore':
        shuffler.restore(args.dirname, args.restore_map)
    else:
        sys.exit()


if __name__ == "__main__":
    main()
