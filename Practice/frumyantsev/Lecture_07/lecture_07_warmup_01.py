class ParagraphReader:

    def __init__(self, file, prgrf_char):
        self._prgrf_char = prgrf_char
        self._par = ''
        self._f = open(file, 'r')
        self._stop_iter = 0
        pass

    def __iter__(self):
        return self

    def __next__(self):
        while self._f:
            self._chr = self._f.read(1)
            if self._stop_iter == 1:
                raise StopIteration
            if self._chr == '':
                self._stop_iter = 1
                return self._par
            elif self._chr == self._prgrf_char:
                res = self._par
                self._par = ''
                return res
            else:
                self._par += self._chr

    def __del__(self):
        self._f.close()


dct_txt = {}
dct_txt[0] = ParagraphReader('text0.txt', 'r')
dct_txt[1] = ParagraphReader('text1.txt', '\n')
dct_txt[2] = ParagraphReader('text2.txt', '\t')

lists = [i for i in range(3)]

dct = {k: [] for k in lists}

for i in range(3):
    for ln in dct_txt[i]:
        dct[i].append(ln)

for k in dct:
    print(dct[k])
