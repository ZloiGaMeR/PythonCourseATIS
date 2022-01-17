class Tank:
    __x = 0  #  _Tank__x
    _speed = 0
    _power = 0

    def shoot(self):
        pass

    def show(self):
        print(f'Tank {type(self)} at {self.__x}')

    def move(self):
        self.__x += self._speed
        # self._Tank__x = self._Tank__x + speed


class T34(Tank):
    _speed = 30
    _power = 30

    def shoot(self):
        print("Ba-bah")


class Tiger(Tank):
    __x = 0  # _Tiger__x
    _speed = 20
    _power = 40

    def shoot(self):
        print("Ba-ba-bah")

    def move(self):
        self.__x += self._speed
        # self._Tiger__x = self._Tiger__x + self._speed


class T90(Tank):
    _speed = 40
    _power = 40

    def shoot(self):
        print("Ba-buh")


class Abrams(T34, Tank):
    _speed = 40
    _power = 40


tanks = [T34(), Tiger(), T90(), Abrams()]
while True:
    for x, y in enumerate(tanks):
        print(f"{x} - {type(y)}")
    i = int(input('Input tank index:'))
    tanks[i].show()
    tanks[i].move()
    tanks[i].shoot()
    tanks[i].show()
    print(tanks[i].__dict__)
    print(type(tanks[i]).__dict__)
    tanks[i]._Tank__x += 1000




