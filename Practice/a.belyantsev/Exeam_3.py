# Создайте класс Money (деньги) для работы с денежными суммами. Число должно быть представлено двумя полями:
# для рублей и для копеек. Дробная часть (копейки) при выводе на экран должна быть отделена от целой части запятой.
# Необходимо реализовать сложение, вычитание, деление сумм и операции сравнения.
# Также нужно добавить атрибут текущий курс по доллару и метод перевода по текущему курсу в доллары


class Money:
    def __init__(self, rubls, pennies):
        self._rubls = rubls
        self._pennies = float(pennies/100)
        self._current_curse = 35

    @property
    def number_of_rubls(self):
        return self._rubls

    @number_of_rubls.setter
    def number_of_rubls(self, value):
        self._rubls = value

    @number_of_rubls.deleter
    def number_of_rubls(self):
        self._rubls = 0

    @property
    def number_of_pennies(self):
        return self._pennies

    @number_of_pennies.setter
    def number_of_pennies(self, value):
        self._pennies = float(value/100)

    @number_of_pennies.deleter
    def number_of_pennies(self):
        self._pennies = 0

    @property
    def current_curse(self):
        return self._current_curse

    @current_curse.setter
    def current_curse(self, value):
        self._current_curse = value

    @current_curse.deleter
    def current_curse(self):
        self._current_curse = 0

    def __str__(self):
        return f"smm is {self._rubls+self._pennies}"

    def __add__(self, other):
        return (self.number_of_rubls + self.number_of_pennies) + (other.number_of_rubls + other.number_of_pennies)

    def __sub__(self, other):  # (x - y).
        return (self.number_of_rubls + self.number_of_pennies) - (other.number_of_rubls + other.number_of_pennies)

    def __mul__(self, other):  # (x * y).
        return (self.number_of_rubls + self.number_of_pennies) * (other.number_of_rubls + other.number_of_pennies)

    def __truediv__(self, other):  # (x / y).
        return (self.number_of_rubls + self.number_of_pennies) / (other.number_of_rubls + other.number_of_pennies)

    def __lt__(self, other):  # x < y
        return (self.number_of_rubls + self.number_of_pennies) < (other.number_of_rubls + other.number_of_pennies)

    def __le__(self, other):  # x ≤ y
        return (self.number_of_rubls + self.number_of_pennies) <= (other.number_of_rubls + other.number_of_pennies)

    def __eq__(self, other):  # x == y
        return (self.number_of_rubls + self.number_of_pennies) == (other.number_of_rubls + other.number_of_pennies)

    def __ne__(self, other):  # x != y
        return (self.number_of_rubls + self.number_of_pennies) != (other.number_of_rubls + other.number_of_pennies)

    def __gt__(self, other):  # x > y
        return (self.number_of_rubls + self.number_of_pennies) > (other.number_of_rubls + other.number_of_pennies)

    def __ge__(self, other):  # x ≥ y
        return (self.number_of_rubls + self.number_of_pennies) >= (other.number_of_rubls + other.number_of_pennies)

    def convertor(self):
        return str((self.number_of_rubls + self.number_of_pennies)/self.current_curse) + " $"


m1 = Money(300, 203)
print(m1)
m2 = Money(1, 1)
print(m2)
print(m1+m2)
print(m1-m2)
print(m1 < m2)
print(m1 > m2)
print(m1/m2)
print(m1.convertor())
