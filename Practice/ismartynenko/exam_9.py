class User:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def getName(self):
        return self.name

    def setName(self, name):
        self.name = name

    def getAge(self):
        return self.age

    def setAge(self, age):
        self.age = age


class Worker(User):
    def __init__(self, name, age, salary):
        super().__init__(name, age)
        self.salary = int(salary)

    def getSalary(self):
        return self.salary

    def setSalary(self, salary):
        self.salary = salary


w1 = Worker(name='John', age='25', salary='1000')
w2 = Worker(name='Jack', age='26', salary='2000')
salary_sum = w1.salary + w2.salary
print(f"{salary_sum=}")
