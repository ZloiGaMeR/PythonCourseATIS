class Reader:
    def __init__(self, p):
        self._sym = "|"
        self._f = open(p, "r")
        self.eof = False

    def __iter__(self):
        return self

    def __next__(self):
        buffer = ""
        char = self._f.read(1)

        if self.eof:
            raise StopIteration

        while char != "":
            if char != self._sym:
                buffer += char
                char = self._f.read(1)
            else:
                break
        else:
            self.eof = True
        return buffer

    def __del__(self):
        self._f.close()


path = "practice7_razminka_1.txt"
for i in Reader(path):
    print(i)
