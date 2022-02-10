class User:
    def __init__(self, name, age):
        self._name = name
        self._age = age

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name):
        self._name = name

    @property
    def age(self):
        return self._age

    @age.setter
    def age(self, age):
        self._age = age


class Worker(User):
    def __init__(self, name, age, salary):
        super().__init__(name, age)
        self._salary = salary

    @property
    def salary(self):
        return int(self._salary)

    @salary.setter
    def salary(self, salary):
        self._salary = salary


w1 = Worker(name='John', age='25', salary='1000')
w2 = Worker(name='Jack', age='26', salary='2000')
salary_sum = w1.salary + w2.salary
print(f"{salary_sum=}")
