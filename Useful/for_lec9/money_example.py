class Money:
    def __init__(self, rub, kop):
        self.rub = rub
        self.kop = kop

    def __add__(self, other):
        rub = self.rub + other.rub
        kop = self.kop + other.kop
        rub += int(kop/100)
        kop = kop % 100
        return Money(rub, kop)

    
m = Money(10, 20)
m1 = Money(10, 30)
m2 = Money(20, 30)
print(m + m1 + m2)
