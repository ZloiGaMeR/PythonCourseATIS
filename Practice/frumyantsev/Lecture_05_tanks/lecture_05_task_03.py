from tempfile import mktemp
import os
import time


class WrapStrToFile:
    _filepath = ''
    _content = ''

    def __init__(self):
        self._filepath = mktemp(dir=os.curdir)

    @property
    def content(self):
        try:
            with open(self._filepath, 'r') as f:
                _content = f.readline()
                return f"{_content}"
        except FileNotFoundError:
            return "Файл пока не создан."
            pass

    @content.setter
    def content(self, value):
        self._filepath = self._filepath
        with open(self._filepath, 'w') as f:
            self._content = f.write(value)

    @content.deleter
    def content(self):
        os.remove(self._filepath)
        pass


if __name__ == "__main__":
    wstf = WrapStrToFile()
    print(wstf.content)  # Output: File doesn't exist
    wstf.content = 'test str'
    print(wstf.content)  # Output: test_str
    wstf.content = 'text 2'
    print(wstf.content)  # Output: text 2
    time.sleep(5)
    del wstf.content  # после этого файла не существуе
