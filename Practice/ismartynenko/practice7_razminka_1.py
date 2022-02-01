class Reader:
    def __init__(self):
        self._sym = "|"
        self._f = open("practice7_razminka_1.txt", "r")

    def __iter__(self):
        return self

    def __next__(self):
        buffer = ""
        char = self._f.read(1)
        while char != "":
            if char != self._sym:
                buffer += char
                char = self._f.read(1)
            else:
                break
        else:
            raise StopIteration
        return buffer

    def __del__(self):
        self._f.close()


for i in Reader():
    print(i)
