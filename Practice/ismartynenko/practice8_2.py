class MyIter:
    def __init__(self, start=0, end=10):
        self._start = start
        self._end = end

    def __iter__(self):
        return self

    def __next__(self):
        self._num = self._start
        if self._num <= self._end:
            self._start += 1
            print(self._num)
            return self._num
        else:
            raise StopIteration

    def show_next(self, n):
        d = self.__dict__.copy()
        lst = []
        for _ in range(n):
            lst.append(next(self))
        self.__dict__ = d
        return lst


c = MyIter(1, 12)
print(f"Print - Three iterations:")
next(c)
next(c)
next(c)
print(f"Print - What are the next 3 numbers:")
c.show_next(3)
print(f"Print - Continue iterations (2):")
next(c)
next(c)
