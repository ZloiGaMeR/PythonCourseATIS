# Реализовать итератор, который бы "читал" заданный текст по параграфам. Символ параграфа задается отдельно

class MyIter:
    def __init__(self, filename, symbol):
        self._symbol = symbol
        self._file = open(filename, 'r')
        self._end = False

    def __iter__(self):
        return self

    def __next__(self):
        out_str = ""
        if self._end is True:
            raise StopIteration
        while True:
            symbol = self._file.read(1)
            if symbol == self._symbol:
                break
            if symbol == "":
                self._end = True
                break
            out_str += symbol
        return out_str

    def __del__(self):
        self._file.close()


for i in MyIter("lec7_text.txt", "@"):
    print(i, end="")
