import random


class Tank:
    # стартовое положение танка (x, y)
    # стартовое положение башни (x, y, x+1, y)
    def __init__(self, x, y):
        self.start_pos_tank = [x, y]
        self.start_pos_tower = [self.start_pos_tank[0], self.start_pos_tank[1],
                                self.start_pos_tank[0] + 1, self.start_pos_tank[1]]

    # движение танка с помощью клавиш W/A/S/D
    def move(self, key, speed):
        if key == 119:
            print("Вы нажали вверх")
            self.start_pos_tank[1] += speed
            self.start_pos_tower[1] += speed
            self.start_pos_tower[3] += speed
            return True
        elif key == 97:
            print("Вы нажали влево")
            self.start_pos_tank[0] -= speed
            self.start_pos_tower[0] -= speed
            self.start_pos_tower[2] -= speed
            return True
        elif key == 115:
            print("Вы нажали вниз")
            self.start_pos_tank[1] -= speed
            self.start_pos_tower[1] -= speed
            self.start_pos_tower[3] -= speed
            return True
        elif key == 100:
            print("Вы нажали вправо")
            self.start_pos_tank[0] += speed
            self.start_pos_tower[0] += speed
            self.start_pos_tower[2] += speed
            return True
        else:
            print("Вы ввели недопустимую команду!")
            return False


# скорость танка
speed = 1

# размеры поля
map_x = 10
map_y = 10

# создание экземпляров танков
a = Tank(random.randint(1, map_x - 1), random.randint(1, map_y - 1))
b = Tank(random.randint(1, map_x - 1), random.randint(1, map_y - 1))

n = int(input("Введите количество ходов: "))
print("Для движения танка используйте клавиши:\n"
      "W/A/S/D - вверх, влево, вниз, вправо соответсвенно.")

for i in range(0, n):
    print("Текущее положение танка A на поле - ", a.start_pos_tank, "и его дула - ", a.start_pos_tower)
    print("Текущее положение танка B на поле - ", b.start_pos_tank, "и его дула - ", b.start_pos_tower)
    key_a = ord(input("Танк A - введите направление движения: "))
    while not a.move(key_a, speed):
        key_a = ord(input("Танк A - введите направление движения: "))

    key_b = ord(input("Танк B - введите направление движения: "))
    while not b.move(key_b, speed):
        key_b = ord(input("Танк B - введите направление движения: "))
