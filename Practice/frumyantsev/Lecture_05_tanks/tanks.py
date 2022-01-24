class Tank:
    __x = 0 # координата
    _speed = 0
    _power = 0

    def shoot(self):
        pass

    def show(self):
        print(f"Tank {self} at {self.__x}")

    def move(self):
        self.__x += self._speed

    def __gt__(self, other):
        return self._power > other._power

    def __ge__(self, other):
        return self._power >= other._power

    def __lt__(self, other):
        return self._power < other._power

    def __le__(self, other):
        return self._power <= other._power

    def __str__(self):
        return self._name

    @property
    def speed(self):
        return self._speed

    @speed.setter
    def speed(self, value):
        self._speed = value

    @property
    def power(self):
        return self._power

    @power.setter
    def power(self, value):
        self._power = value

    @property
    def x(self):
        return self.__x

    @x.setter
    def x(self, value):
        self.__x = value


class T34(Tank):
    _name = "T34"
    _speed = 30
    _power = 30

    def shoot(self):
        print("Ba-bah")


class Tiger(Tank):
    _name = "Tiger"
    _speed = 20
    _power = 40

    def shoot(self):
        print("Ba-ba-bah")


class T90(Tank):
    _name = "T90"
    _speed = 40
    _power = 40

    def shoot(self):
        print("Ba-buh")


class Abrams(Tank):
    _name = "Abrams"
    _speed = 40
    _power = 40

    def shoot(self):
        print("Ba-buh")


if __name__ == "__main__":
    tanks = [T34(), Tiger(), T90(), Abrams()] # список из экземпляров
    while True:
        for x, y in enumerate(tanks):
            print(f"{x} - {type(y)}")
        i = int(input('Input tank index: '))
        tanks[i].show()
        tanks[i].move()
        tanks[i].shoot()
        tanks[i].show()
        print(tanks[i].__dict__)
        print(type(tanks[i]).__dict__)
        tanks[i]._Tank__x += 1000
        tanks[i].show()

