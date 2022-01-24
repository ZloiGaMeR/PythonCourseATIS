import time
import random
from practice5_1_classMan import Man


class Pupil(Man):
    def solve_task(self):
        sec = random.randint(3, 6)
        time.sleep(sec)
        super().solve_task()


e1 = Man("John")
print(e1.name, e1.solve_task())

e2 = Pupil("Tim")
print(e2.name, e2.solve_task())
