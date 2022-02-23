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
            return self._num
        else:
            raise StopIteration


for i in MyIter():
    print(i)
