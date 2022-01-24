import time
import random


class Man:
    _name = ''

    def __init__(self, name):
        self._name = name

    @staticmethod
    def solve_task():
        print("I'm not ready yet")

    @property
    def name(self):
        return self._name


class Pupil(Man):
    def solve_task(self):
        time.sleep(random.randint(3, 6))
        super().solve_task()


m1 = Man("Joe")
print(m1.name)
m1.solve_task()

p1 = Pupil("Jake")
print(p1.name)
p1.solve_task()
