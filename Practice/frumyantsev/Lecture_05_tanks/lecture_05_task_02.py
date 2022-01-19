import time
import random


class Man:
    name = ''

    def __init__(self):
        self.name = input("Введите имя: ")

    # @staticmethod
    def solve_task(self):
        print("I'm not ready yet")


class Pupil(Man):
    def solve_task(self):
        time.sleep(random.randint(3, 6))
        print("I'm not ready yet")


m1 = Man()
print(m1.name)
m1.solve_task()

p1 =Pupil()
print(p1.name)
p1.solve_task()