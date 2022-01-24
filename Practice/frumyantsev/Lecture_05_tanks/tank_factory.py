# 1.
# Написать функцию-фабрику танков.
# Принимает {тип: количество танков}: {T34: 5, Tiger: 10}
# Возвращает отсортированный по мощи (power) список танков.

# 2.
# + принимает значения скорости (speed), мощи (power) и начальной координаты (x).
# + Устанавливает переданные значения для всех танков.

import tanks


def factory(d):
    lst_tanks = []
    for k, v in d.items():
        lst_tanks += [k() for _ in range(v)]
        # for _ in range(v):
        #     # print(f"{k=}, {v=}")
        #     new_tank = k()
        #     lst_tanks.append(new_tank)
    # lst_tanks = sorted(lst_tanks, key=lambda x: x.power)
    lst_tanks.sort()
    print(f"Список созданных танков, отсортированный по мощи:\n{lst_tanks}")

    # 2. не использовал метод __init__ чтобы сохранилась первая часть задания
    passed_speed = int(input("\nУкажите новую скорость для всех создаваемых танков: "))
    passed_power = int(input("Укажите новую мощь для всех создаваемых танков: "))
    passed_coord = int(input("Укажите новую начальную координату для всех создаваемых танков: "))
    for tank in lst_tanks:
        tank.speed = passed_speed
        tank.power = passed_power
        tank.x = passed_coord
    print(f"\nСписок созданных танков, с измененными ТТХ:\n{lst_tanks}\n")
    for tank in lst_tanks:
        tank.show()
        print(f"New tank speed: {tank.speed}; new tank power: {tank.power}\n")

    return None


if __name__ == "__main__":
    dicti = {tanks.Abrams: 2, tanks.T34: 3, tanks.Tiger: 1}
    lst = factory(dicti)
