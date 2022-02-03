class Reader:
    def __init__(self, p):
        self._sym = "|"
        self._f = open(p, "r")
        self._eof = False

    def __iter__(self):
        return self

    def __next__(self):
        if self._eof:
            raise StopIteration

        buffer = ""
        char = self._f.read(1)
        while char != "":
            if char != self._sym:
                buffer += char
                char = self._f.read(1)
            else:
                break
        else:
            self._eof = True
        return buffer

    def __del__(self):
        self._f.close()


path = "practice7_razminka_1.txt"
for i in Reader(path):
    print(i)
