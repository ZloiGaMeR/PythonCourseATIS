class Position:
    def __init__(self, money):
        self.money = money


class Employee:
    def __init__(self, name, surname, salary, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._name = name
        self._surname = surname
        self._salary = salary
        self.__free_time = 0
        self._position = Position(salary)

    def say_hello(self):
        print('Hello')

    def __repr__(self):
        return f"Employee {self._name} {self._surname} with {self.__free_time}"


class TaxPayer:
    def __init__(self, state, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._state = state


class Manager(Employee, TaxPayer):
    def __init__(self, name, surname, salary, state, employees=tuple()):
        super().__init__(name, surname, salary, state)
        # Альтернативный вызов конструкторов, если в родительских
        # классах не предусмотрены вызовы super().__init__(*args, **kwargs):
        # super().__init__(name, surname, salary)
        # super(Employee, self).__init__(state)
        self._employees = employees

    def __repr__(self):
        return f"Manager {self._name} {self._surname}"


e1 = Employee("Ivan", "Ivanov", 50000)
m = Manager("Petr", "Petrov", 100000, 'Russia', (e1,))
print(m._state)
