# Создайте класс Money (деньги) для работы с денежными суммами. Число должно быть представлено двумя полями:
# для рублей и для копеек. Дробная часть (копейки) при выводе на экран должна быть отделена от целой части запятой.
# Необходимо реализовать сложение, вычитание, деление сумм и операции сравнения.
# Также нужно добавить атрибут текущий курс по доллару и метод перевода по текущему курсу в доллары


class Money:
    def __init__(self, rubls, pennies):
        self._rubls = rubls
        self._pennies = pennies
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
        self._pennies = value

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
        return f"smm is {self._rubls + float(self._pennies/100)}"

    def __add__(self, other):
        _m = Money(0, 0)
        _m.number_of_rubls = self.number_of_rubls + other.number_of_rubls
        _m.number_of_pennies = self.number_of_pennies + other.number_of_pennies
        return _m

    def __sub__(self, other):  # (x - y).
        _m = Money(0, 0)
        _m.number_of_rubls = self.number_of_rubls - other.number_of_rubls
        _m.number_of_pennies = self.number_of_pennies - other.number_of_pennies
        return _m

    def __mul__(self, other):  # (x * y).
        _m = Money(0, 0)
        _m.number_of_rubls = self.number_of_rubls * other.number_of_rubls
        _m.number_of_pennies = self.number_of_pennies * other.number_of_pennies
        return _m

    def __truediv__(self, other):  # (x / y).
        _m = Money(0, 0)
        _m.number_of_rubls = self.number_of_rubls / other.number_of_rubls
        _m.number_of_pennies = self.number_of_pennies / other.number_of_pennies
        return _m

    def __lt__(self, other):  # x < y
        return (self.number_of_rubls + float(self.number_of_pennies/100)) < \
               (other.number_of_rubls + float(other.number_of_pennies/100))

    def __le__(self, other):  # x ≤ y
        return (self.number_of_rubls + float(self.number_of_pennies/100)) <= \
               (other.number_of_rubls + float(other.number_of_pennies/100))

    def __eq__(self, other):  # x == y
        return (self.number_of_rubls + float(self.number_of_pennies/100)) == \
               (other.number_of_rubls + float(other.number_of_pennies/100))

    def __ne__(self, other):  # x != y
        return (self.number_of_rubls + float(self.number_of_pennies/100)) != \
               (other.number_of_rubls + float(other.number_of_pennies/100))

    def __gt__(self, other):  # x > y
        return (self.number_of_rubls + float(self.number_of_pennies/100)) > \
               (other.number_of_rubls + float(other.number_of_pennies/100))

    def __ge__(self, other):  # x ≥ y
        return (self.number_of_rubls + float(self.number_of_pennies/100)) >= \
               (other.number_of_rubls + float(other.number_of_pennies/100))

    def convertor(self):
        return str((self.number_of_rubls + float(self.number_of_pennies/100))/self.current_curse) + " $"


m1 = Money(0, 0)
# print(m1)
m2 = Money(1, 10)
m3 = Money(2, 20)
# print(m2)
m = m1 + m2 + m3
print(m)
print(type(m))
# print(m1-m2)
print(m1 < m2)
print(m1 > m2)
print(m1/m2)
print(m1.convertor())
