class GameSetup:
    '''
    Класс настроек игры
    MAX_* - константы ограничивающие максимальное значение параметра
    rank_val - словарь званий
    '''
    MAX_TANK_HP = 300
    MAX_TANK_SPEED = 10
    MAX_TANK_ROT_SPEED = 10
    MAX_TANK_WEAPON_POWER = 30
    RANK_VAL = {'Примарх': 6, 'Магистр Ордена': 5, 'Библиарий': 4, 'Капелан': 3, 'Командир роты': 2, 'Боевой брат': 1}


class Tank:
    '''
    Класс описывающий параметры танка
    '''
    def __init__(self, name, hp, speed, rotation_speed, weapon_power):
        self.name = name
        self.hp = hp
        self.speed = speed
        self.rotation_speed = rotation_speed
        self.weapon_power = weapon_power
        if self.hp > GameSetup.MAX_TANK_HP:
            self.hp = GameSetup.MAX_TANK_HP
        if self.speed > GameSetup.MAX_TANK_SPEED:
            self.speed = GameSetup.MAX_TANK_SPEED
        if self.rotation_speed > GameSetup.MAX_TANK_ROT_SPEED:
            self.rotation_speed = GameSetup.MAX_TANK_ROT_SPEED
        if self.weapon_power > GameSetup.MAX_TANK_WEAPON_POWER:
            self.weapon_power = GameSetup.MAX_TANK_WEAPON_POWER

    def power(self):
        '''
        Функция подсчёта мощности танка, в зависимости от его параметров
        '''
        return self.hp * self.speed * self.rotation_speed * self.weapon_power

    def info(self):
        '''
        Функция выводящая на печать ТТХ танка
        '''
        print(f"Название танка: {self.name}")
        print(f"Количество жизней: {self.hp}")
        print(f"Скорость танка: {self.speed}")
        print(f"Скорость поворота: {self.rotation_speed}")
        print(f"Мощность орудия: {self.weapon_power}")
        print(f"Суммарная мощность танка: {self.power()}")

    def __gt__(self, other):
        '''
        Функция для сравнения мощности двух танков
        '''
        return self.power() > other.power()


class Commander:
    '''
    Класс описывающий параметры командиров
    '''
    def __init__(self, full_name, nickname, rank, exp, accuracy, familiarity_tank):
        self.full_name = full_name
        self.nickname = nickname
        self.rank = rank
        self.exp = exp
        self.accuracy = accuracy
        self.familiarity_tank = familiarity_tank

    def power(self):
        '''
        Функция подсчёта мощности командира, в зависимости от его параметров
        '''
        return GameSetup.RANK_VAL.get(self.rank, 0.5) * self.exp * self.accuracy * self.familiarity_tank

    def info(self):
        '''
        Функция выводит описание командира
        '''
        print(f"Имя командира: {self.full_name}")
        print(f"Прозвище: {self.nickname}")
        print(f"Звание: {self.rank}")
        print(f"Опыт: {self.exp}")
        print(f"Меткость: {self.accuracy}")
        print(f"Уровень владения танком: {self.familiarity_tank}")


class Battleground:
    '''
    Класс описывающий поле боя
    '''
    def __init__(self, time_of_day, weather, landscape):
        self.time_of_day = time_of_day
        self.weather = weather
        self.landscape = landscape

    def info(self):
        '''
        Функция выводит описание поля боя
        '''
        print(f"Время: {self.time_of_day}")
        print(f"Погода: {self.weather}")
        print(f"Ландшафт: {self.landscape}")


Tank1 = Tank("Хищник", 100, 5, 5, 15)
Tank1.info()
Tank2 = Tank("Лендрейдер", 600, 3, 2, 30)
Tank2.info()
print(f"{Tank1.name=} мощнее чем {Tank2.name=} ? {Tank1 > Tank2}")
Commander1 = Commander("Эзекиль Аббадон", "Разоритель", "Магистр Ордена", 100000, 1, 1)
Commander1.info()
print(f"Мощь командира: {Commander1.power()}")
Commander2 = Commander("Леман Русс", "Жопашник", "Примарх", 9999999999, 1, 1)
Commander2.info()
print(f"Мощь командира: {Commander2.power()}")
