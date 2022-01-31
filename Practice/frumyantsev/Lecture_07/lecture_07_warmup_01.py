# import datetime


class ParagraphReader:

    def __init__(self, file, prgrf_char):
        self.lst = []
        self.file = file
        self.prgrf_char = prgrf_char
        self.i = 0
        self.par = ''
        # print(self.prgrf_char)
        pass

    def __iter__(self):
        return self

    def __next__(self):
        with open(self.file, 'r') as f:
            try:
                chr = f.read()[self.i]
                # print(f"{chr=}")
                if chr != self.prgrf_char:
                    self.par += chr
                    self.i += 1
                else:
                    self.i += 1
                    res = self.par
                    self.par = ''
                    return res
                # print(f"{self.i=}")
            except IndexError:
                # print("IndexError")
                raise StopIteration
        # print(f"{self.par=}")


txt1 = ParagraphReader('text0', 'r')

lst = []
for ln in txt1:
    if ln:
        lst.append(ln)

print(lst)
