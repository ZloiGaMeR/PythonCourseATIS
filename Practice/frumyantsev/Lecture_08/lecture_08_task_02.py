import math


class MyIterator:
    def __init__(self, limit):
        self.start = 0
        self.step = 3
        self.limit = limit

    def __iter__(self):
        return self

    def __next__(self):
        if self.start < self.limit:
            res = self.start
            self.start += self.step
            return res
        raise StopIteration

    def preview(self, qty):
        prvw_lst = []
        qty_actual = min(qty, math.ceil((self.limit - self.start)/self.step))
        for j in range(qty_actual):
            prvw_lst.append(self.start + self.step * j)
        return f"Previewing {qty_actual} elements of iterator: {prvw_lst}"


mi1 = MyIterator(28)
for i in mi1:
    print(i)
    if i == 18:
        print(mi1.preview(5))
