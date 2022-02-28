class Money:
    rate = 1

    def __init__(self, integer=0, fraction=0):
        self._integer = integer
        self._fraction = fraction

    @staticmethod
    def make_from_str(money_str):
        m = Money()
        money_list = money_str.split('.')
        if len(money_list) > 0:
            m._integer = int(money_list[0])
            if len(money_list) > 1:
                m._fraction = int(money_list[1])
        return m

    def to_float(self):
        return float('{}.{}'.format(self._integer, self._fraction))

    def __repr__(self):
        return '{},{}'.format(self._integer, self._fraction)

    def __add__(self, other):
        sum_num = self.to_float() + other.to_float()
        return Money.make_from_str(str(sum_num))

    def __sub__(self, other):
        sum_num = self.to_float() - other.to_float()
        return Money.make_from_str(str(sum_num))

    def __truediv__(self, other):
        if isinstance(other, Money):
            sum_num = self.to_float()/other.to_float()
        else:
            sum_num = self.to_float()/other
        this_num = self._integer * 100 + self._fraction
        return Money.make_from_str(str(sum_num))

    def __lt__(self, other):
        res = False
        if self._integer < other._integer:
            res = True
        elif self._integer == other._integer:
            res = self._fraction < other._fraction
        return res

    def __gt__(self, other):
        res = False
        if self._integer > other._integer:
            res = True
        elif self._integer == other._integer:
            res = self._fraction > other._fraction
        return res

    def __le__(self, other):
        res = False
        if self._integer < other._integer:
            res = True
        elif self._integer == other._integer:
            res = self._fraction <= other._fraction
        return res

    def __ge__(self, other):
        res = False
        if self._integer > other._integer:
            res = True
        elif self._integer == other._integer:
            res = self._fraction >= other._fraction
        return res

    def __eq__(self, other):
        if self._integer == other._integer and \
                        self._fraction == other._fraction:
            res = True
        else:
            res = False

    def __ne__(self, other):
        return not self.__eq__(other)

    def to_dollars(self):
        dol = self.to_float() / Money.rate
        return str(Money.make_from_str(str(dol)))


if __name__ == '__main__':
    m1 = Money(10, 50)
    m2 = Money(100, 125)
    print('m1 = ', m1)
    print('m2 = ', m2)
    print('{} + {} = {}'.format(m1, m2, m1+m2))
    print('{} - {} = {}'.format(m1, m2, m1-m2))
    print('{} / {} = {}'.format(m1, m2, m1/m2))
    print('{} < {} = {}'.format(m1, m2, m1<m2))
    print('{} > {} = {}'.format(m1, m2, m1>m2))
    print('{} <= {} = {}'.format(m1, m2, m1<=m2))
    print('{} >= {} = {}'.format(m1, m2, m1>=m2))
    Money.rate = 60
    print('{} to dollars = {}'.format(m1, m1.to_dollars()))
    print('{} to dollars = {}'.format(m2, m2.to_dollars()))
