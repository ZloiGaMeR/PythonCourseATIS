# Написать класс WrapStrToFIle, который будет иметь одно вычисляемое свойство (property) под названием content.
# В конструкторе класс должен инициализовать атрибут filepath, путем присваивания результата функции
# mktemp  библиотеки tempfile. При попытке чтения свойства content должен внутри кода свойства открываться файл,
# используя атрибут filepath (с помощью функции open, из этого файла читается все содержимое и возвращается из свойства.
# Если файл не существует, то возникает ошибка, поэтому должна быть обертка вокруг открытия файла на
# чтение (try...except), с помощью которого будет возвращаться 'Файл еще не существует'. При присваивании значения
# свойству content файл по указанному пути должен открываться на запись и записываться содержимое. Не забудьте
# закрывать файл после чтения или записи. При удалении атрибута content, должен удаляться и файл.
import os
import tempfile


class WrapStrToFile:
    def __init__(self):
        self.filepath = tempfile.mktemp()
        # здесь инициализируется атрибут filepath, он содержит путь до файла-хранилища

    @property
    def content(self):
        try:
            f = open(self.filepath, "r")
            temp = f.read()
            f.close()
            return temp
        except FileNotFoundError:
            print("File doesn't exist")

        # попытка чтения из файла, в случае успеха возвращаем содержимое
        # в случае неудачи возвращаем 'File doesn't exist'

    @content.setter
    def content(self, value):
        f = open(self.filepath, "w")
        f.write(value)
        f.close()
        # попытка записи в файл указанного содержимого

    @content.deleter
    def content(self):
        os.remove(self.filepath)
        # удаляем файл: os.remove(имя_файла)


wstf = WrapStrToFile()
print(wstf.content)  # Output: File doesn't exist
wstf.content = 'test str'
print(wstf.content)  # Output: test_str
wstf.content = 'text 2'
print(wstf.content)  # Output: text 2
del wstf.content     # после этого файла не существует
