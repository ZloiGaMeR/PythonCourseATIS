class Employee:
    # first_name = 'James'
    # last_name = 'Bond'

    def __init__(self, first_name, last_name, salary):
        self.first_name = first_name
        self.last_name = last_name
        self.salary = salary

    def say_my_name(self):
        print(f"{self.first_name=}, {self.last_name=}")

    def __add__(self, other):
        return self.salary + other.salary


def total_count(*emps):
    s = 0
    for each in emps:
        s += each.salary
    print(s)


emp1 = Employee('John', 'Doe', 200000)
emp2 = Employee('John1', 'Doe1', 400000)

emp1.buh('John', 'Doe', 200000)
emp2.buh('John1', 'Doe1', 400000)

print(emp1 + emp2)

#
# emp1.say_my_name()
# emp2.say_my_name()
#
# Employee.salary = 100000
# emp1.salary = 50000
# #print(emp2.salary)
#
# total_count(emp1, emp2)

