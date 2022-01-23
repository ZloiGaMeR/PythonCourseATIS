class Man:
    def __init__(self, name):
        self.name = name

    @staticmethod
    def solve_task():
        return "I'm not ready yet"


e = Man("John")
print(e.name, Man.solve_task())
