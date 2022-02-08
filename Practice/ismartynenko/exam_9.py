class User:
    def __init__(self, name, age):
        self.__name = name
        self.__age = age

    def getName(self):
        return self.__name

    def setName(self, name):
        self.__name = name

    def getAge(self):
        return self.__age

    def setAge(self, age):
        self.__age = age


class Worker(User):
    def __init__(self, name, age, salary):
        super().__init__(name, age)
        self.__salary = salary

    @property
    def getSalary(self):
        return int(self.__salary)

    def setSalary(self, salary):
        self.__salary = salary


w1 = Worker(name='John', age='25', salary='1000')
w2 = Worker(name='Jack', age='26', salary='2000')
salary_sum = w1.getSalary + w2.getSalary
print(f"{salary_sum=}")
