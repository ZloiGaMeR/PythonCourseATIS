class ParagraphReader:

    def __init__(self, file, prgrf_char):
        self._prgrf_char = prgrf_char
        self._par = ''
        self._f = open(file, 'r')
        self._stop_iter = False

    def __iter__(self):
        return self

    def __next__(self):
        while not self._stop_iter:
            self._chr = self._f.read(1)
            if self._chr == '':
                self._stop_iter = True
                return self._par
            elif self._chr == self._prgrf_char:
                res = self._par
                self._par = ''
                return res
            else:
                self._par += self._chr
        raise StopIteration

    def __del__(self):
        self._f.close()


lst_txt = []
lst_txt.append(ParagraphReader('text0.txt', 'r'))
lst_txt.append(ParagraphReader('text1.txt', '\n'))
lst_txt.append(ParagraphReader('text2.txt', '\t'))

lists = []
for it in lst_txt:
    lst = []
    for ln in it:
        lst.append(ln)
    lists.append(lst)

for lst in lists:
    print(lst)
