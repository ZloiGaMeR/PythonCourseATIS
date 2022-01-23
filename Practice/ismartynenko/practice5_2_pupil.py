import time
import random


class Man:
    def __init__(self, name):
        self.name = name

    @staticmethod
    def solve_task():
        return "I'm not ready yet"


class Pupil(Man):
    sec = random.randint(3, 6)
    time.sleep(sec)
    Man.solve_task()


e1 = Man("John")
print(e1.name, Man.solve_task())

e2 = Pupil("Tim")
print(e2.name, Pupil.solve_task())
