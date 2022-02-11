# Создайте класс Money (деньги) для работы с денежными суммами. Число должно быть представлено двумя полями:
# для рублей и для копеек. Дробная часть (копейки) при выводе на экран должна быть отделена от целой части запятой.
# Необходимо реализовать сложение, вычитание, деление сумм и операции сравнения.
# Также нужно добавить атрибут текущий курс по доллару и метод перевода по текущему курсу в доллары
import math as _math


class Money:
    def __init__(self, rubles, pennies):
        if isinstance(pennies, int):
            tmp = _math.modf(rubles + float(pennies/100))
            self._rubles = tmp[1]
            self._pennies = tmp[0]
        else:
            self._rubles = rubles
            self._pennies = pennies
        self._current_curse = 35

    @property
    def number_of_rubles(self):
        return self._rubles

    @number_of_rubles.setter
    def number_of_rubles(self, value):
        self._rubles = value

    @number_of_rubles.deleter
    def number_of_rubles(self):
        self._rubles = 0

    @property
    def number_of_pennies(self):
        return self._pennies

    @number_of_pennies.setter
    def number_of_pennies(self, value):
        if isinstance(value, int):
            tmp = _math.modf(float(value/100))
            self._rubles += tmp[1]
            self._pennies = tmp[0]
        else:
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
        return f"smm is {round(self._rubles + self._pennies,2)}"

    def __repr__(self):
        return self._rubles + self._pennies

    def __add__(self, other):
        rubles = self.number_of_rubles + other.number_of_rubles
        pennies = self.number_of_pennies + other.number_of_pennies
        return Money(rubles, pennies)

    def __sub__(self, other):  # (x - y).
        rubles = self.number_of_rubles - other.number_of_rubles
        pennies = self.number_of_pennies - other.number_of_pennies
        return Money(rubles, pennies)

    def __mul__(self, other):  # (x * y).
        rubles = self.number_of_rubles * other.number_of_rubles
        pennies = self.number_of_pennies * other.number_of_pennies
        return Money(rubles, pennies)

    def __truediv__(self, other):  # (x / y).
        rubles = self.number_of_rubles / other.number_of_rubles
        pennies = self.number_of_pennies / other.number_of_pennies
        return Money(rubles, pennies)

    def __lt__(self, other):  # x < y
        return (self.number_of_rubles + float(self.number_of_pennies/100)) < \
               (other.number_of_rubles + float(other.number_of_pennies/100))

    def __le__(self, other):  # x ≤ y
        return (self.number_of_rubles + float(self.number_of_pennies/100)) <= \
               (other.number_of_rubles + float(other.number_of_pennies/100))

    def __eq__(self, other):  # x == y
        return (self.number_of_rubles + float(self.number_of_pennies/100)) == \
               (other.number_of_rubles + float(other.number_of_pennies/100))

    def __ne__(self, other):  # x != y
        return (self.number_of_rubles + float(self.number_of_pennies/100)) != \
               (other.number_of_rubles + float(other.number_of_pennies/100))

    def __gt__(self, other):  # x > y
        return (self.number_of_rubles + float(self.number_of_pennies/100)) > \
               (other.number_of_rubles + float(other.number_of_pennies/100))

    def __ge__(self, other):  # x ≥ y
        return (self.number_of_rubles + float(self.number_of_pennies/100)) >= \
               (other.number_of_rubls + float(other.number_of_pennies/100))

    def convertor(self):
        return str((self.number_of_rubles + self.number_of_pennies)/self.current_curse) + " $"


m1 = Money(26, 0)
m1.number_of_pennies = 900
print(m1)
m2 = Money(1, 10)
m3 = Money(2, 310)
# print(m2)
m = m1 + m2 - m3
print(m)
# print(type(m))
# print(m1-m2)
# print(m1 < m2)
# print(m1 > m2)
# print(m1/m2)
print(m1.convertor())
