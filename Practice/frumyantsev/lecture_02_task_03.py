WEATHER = ["rain", "fog", "sun"]
MODEL = ["T34", "BT", "Panther", "Abrams", "Leopard"]
TIME_OF_DAY = ["morning", "day", "evening", "night"]
DIRECTION = ["forward", "backward"]
MAP = ["map1", "map2"]
ARMY = ["Soviet", "German", "US", "France", "UK"]


class Tank:
    def __init__(self, load_regular : int, load_explosive : int, model = 'T34', technical_state = '10'):
        self.model = model
        self.technical_state = technical_state # should vary from 10 (new tank) to 0 (completely destroyed)
        self.load_regular = load_regular # regular weapon load
        self.load_explosive = load_explosive # explosive weapon load
        return None

    def tank_turn(self, angle):
        """
        Движение за счет одной гусеницы танка.
        Танк совершает вращение вокруг центра неприводимой в движение гусеницы.
        """
        self.angle = angle # from -180 degrees to +180 degrees
        return self.angle

    def tank_rotate(self, angle):
        """
        Движение за счет двух гусениц танка. Танк совершает вращение вокруг своего центра.
        """
        self.angle = angle # from -180 degrees to +180 degrees
        return self.angle

    def roll(self, direction, speed):
        """ Движение танка вперед или назад. """
        self.direction = direction # forward and backward
        self.speed = speed
        return self.speed, self.direction

    def fire(self, fire_angle, projectile):
        self.fire_angle = fire_angle # from -5 degrees to +45 degrees
        self.projectile = projectile # regular, explosive
        return self.fire_angle, self.projectile

    def rotate_turret(self, angle): # from -180 degrees to +180 degrees
        self.angle = angle

class Battlefield:
    def __init__(self, map = MAP[0], weather = WEATHER[0], time_of_day = TIME_OF_DAY[0]):
        self.map = map
        self.weather = weather
        self.time_of_day = time_of_day
        print(f"{self.map=}")
        print(f"{self.weather=}")
        print(f"{self.time_of_day=}")

    def change_weather(self,weather):
        return None # ???


class Map:
    def __init__(self, terrain, width, length):
        self.terrain = terrain
        self.width = width
        self.length = length

class Army:
    def __init__(self, army = ARMY[0]):
        self.army = army

class Position:
    def __init__(self, coordinate_x, coodrinate_y, orientation):
        self.coordinate_x = coordinate_x
        self.coordinate_y = coodrinate_y
        self.orientation = orientation

class HeavyTank(Tank):
    def __init__(self, extra_armor):
        self.extra_armor = extra_armor

print(Tank.tank_turn.__doc__)
print(Tank.tank_rotate.__doc__)

battlefield_1 = Battlefield()
tank_1 = Tank(5, 5)
heavy_tank_1 = HeavyTank("armor_level_5")
# не понятно, почему при создании нового объекта дочернего класса HeavyTank не потребовалось
# задавать переменные load_regular, load_explosive родительского класса Tank
print(tank_1.__dict__)
print(heavy_tank_1.__dict__)