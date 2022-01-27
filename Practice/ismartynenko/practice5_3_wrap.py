import os
from tempfile import mktemp


class WrapStrToFile:
    def __init__(self): 
        # здесь инициализируется атрибут filepath, он содержит путь до файла-хранилища
        self.filepath = mktemp()

    @property 
    def content(self): 
        # попытка чтения из файла, в случае успеха возвращаем содержимое 
        # в случае неудачи возвращаем 'File doesn't exist'
        try:
            with open(self.filepath, "r") as fp:
                text = fp.read()
        except FileNotFoundError:
            print("File doesn't exist")
        else:
            return text

    @content.setter
    def content(self, value): 
        # попытка записи в файл указанного содержимого
        with open(self.filepath, "w+") as fp:
            fp.write(value)

    @content.deleter 
    def content(self): 
        # удаляем файл: os.remove(имя_файла)
        os.remove(self.filepath)


wstf = WrapStrToFile()
print(wstf.content)  # Output: File doesn't exist
wstf.content = 'test str'
print(wstf.content)  # Output: test_str 
wstf.content = 'text 2' 
print(wstf.content)  # Output: text 2 
del wstf.content     # после этого файла не существует
