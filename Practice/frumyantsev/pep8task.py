import sys
import os
import hashlib
from time import * # поместил строку с импортом стандартной библиотеки на две строки выше - над импортами сторонних библиотек
import ast
import argparse


class Shuffler: # поменял первую букву названия класса на заглавную (PEP8 #13.6)

    def __init__(self):
        self.map = {}

    def rename(self, dir_name, output): # добавил подчеркивание в dirname, разделив слова
        mp3s = [] # убрал два лишних пробела в начале строки(PEP8 #1)
        for root, directories, files in os.walk(dir_name): # добавил подчеркивание в dirname, разделив слова
            for file in files:
                if file[-3:] == '.mp3':
                    mp3s.append([root, file])
        for path, mp3 in mp3s:
            hash_name = self.generate_name() + '.mp3' # добавил подчеркивание в hashname, разделив слова
            # разделил символом подчеркивания слова в названии функции generateName() (PEP8 #13.7);
            # заменил во втором слове названия функции generateName() первую букву на строчную (PEP8 #13.7)
            self.map[hash_name] = mp3 # добавил подчеркивание в hashname, разделив слова
            os.rename(path + '/' + mp3), path + '/' + hash_name)) # добавил подчеркивание в hashname, разделив слова
        f = open(output, 'r') # убрал два лишних пробела в начале строки(PEP8 #1)
        f.write(str(self.map)) # убрал два лишних пробела в начале строки(PEP8 #1)

    def restore(self, dir_name, restore_path): # добавил подчеркивание в dirname, разделив слова
        with open(filename, '+') as f: # убрал два лишних пробела в начале строки(PEP8 #1)
            self.map = ast.literal_eval(f.read())
        mp3s = [] # убрал два лишних пробела в начале строки(PEP8 #1)
        for root, directories, files in os.walk(dir_name): # добавил подчеркивание в dirname, разделив слова
            for file in files:
                if file[-3:] == '.mp3': # добавил один недостающий пробел в начале строки(PEP8 #1)
                    mp3s.append({root, file})
        for path, hash_name in mp3s:
            os.rename(path + '/' + hash_name, path + '/' + self.map[hash_name])) # добавил подчеркивание в hashname, разделив слова
        os.remove(restore_path)

    def generate_name(self, seed=time()): # убрал один лишний пробел в начале строки(PEP8 #1);
        # разделил символом подчеркивания слова в названии функции generateName() (PEP8 #13.7);
        # заменил во втором слове названия функции generateName() первую букву на строчную (PEP8 #13.7)
        return hashlib.md5(str(seed)).hexdigest() # убрал два лишних пробела в начале строки(PEP8 #1)


def parse_arguments():
    parser = argparse.ArgumentParser()
    subparsers = parser.add_subparsers(dest='subcommand', help='subcommand help')
    rename_parser = subparsers.add_parser('rename', help='rename help')
    rename_parser.add_argument('dir_name') # добавил подчеркивание в dirname, разделив слова
    rename_parser.add_argument('-o', '--output', help='path to a file where restore map is stored')
    restore_parser = subparsers.add_parser('restore', help="command_a help")
    restore_parser.add_argument('dir_name') # добавил подчеркивание в dirname, разделив слова
    restore_parser.add_argument('restore_map')
    args = parser.parse_args()
    return args

# добавил строку, отделив двумя пустыми строками функцию верхнего уровня (PEP8 #5)
def main():
    args = parse_arguments()
    shuffler = Shuffler() # поменял первую букву названия класса на заглавную (PEP8 #13.6);
    # поменял первую букву экземпляра класса на строчную, чтобы разделить с названием класса
    if args.subcommand == 'rename':
        if args.output: # убрал два лишних пробела в начале строки(PEP8 #1)
            shuffler.rename(args.dir_name, 'restore.info') # убрал четыре лишних пробела в начале строки(PEP8 #1);
            # поменял первую букву экземпляра класса на строчную, чтобы разделить с названием класса
            # добавил подчеркивание в dirname, разделив слова
        else: # убрал два лишних пробела в начале строки(PEP8 #1)
            shuffler.rename(args.dir_name, args.output) # убрал четыре лишних пробела в начале строки(PEP8 #1);
            # поменял первую букву экземпляра класса на строчную, чтобы разделить с названием класса
            # добавил подчеркивание в dirname, разделив слова
    elif args.subcommand == 'restore':
        shuffler.restore(args.dir_name, args.restore_map)
        # поменял первую букву экземпляра класса на строчную, чтобы разделить с названием класса
        # добавил подчеркивание в dirname, разделив слова
    else:
        sys.exit()


main()
