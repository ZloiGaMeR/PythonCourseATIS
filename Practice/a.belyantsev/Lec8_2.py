# Реализовать итератор с возможностью просмотра следующего элемента или набора элементов не меняя состояние итератора.
class MyIter:
    def __init__(self, in_lst):
        self._index = 0
        self._lst = in_lst
        self._len = len(in_lst)

    def __iter__(self):
        return self

    def __next__(self):
        if self._index < self._len:
            out = self._lst[self._index]
            self._index += 1
            return out
        else:
            raise StopIteration

    def show_next(self, n):
        return self._lst[self._index:self._index+n]


i = MyIter([1, 2, 3, 4, 5, 6, 7, 8, 9])
print(next(i))
print(i.show_next(2))
print(next(i))
print(i.show_next(2))
print(next(i))
print(next(i))
print(next(i))
print(next(i))


