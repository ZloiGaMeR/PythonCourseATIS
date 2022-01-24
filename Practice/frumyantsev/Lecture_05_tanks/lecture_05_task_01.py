class Man:
    _name = 'Not Defined'

    def __init__(self, name):
        self._name = name

    @staticmethod
    def solve_task():
        print("I'm not ready yet")

    @property
    def name(self):
        return self._name


m1 = Man("John")
print(m1.name)
m1.solve_task()
