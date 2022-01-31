# Написать собственную реализацию встроенной функции enumerate().
# Она применяется для итерируемых коллекций (строки, списки, словари и др.) и
# создает объект, который генерирует кортежи, состоящие из двух элементов - индекса элемента и самого элемента:
#
# >>> a = [10, 20, 30, 40]
# >>> for i in enumerate(a):
# ...     print(i)
# ...
# (0, 10)
# (1, 20)
# (2, 30)
# (3, 40)
def myenumerate(in_str):
    out_str = list()
    count = 0
    for i in in_str:
        out_str.append((count, i))
        count += 1
    return out_str


print("mynumerate")
a = [10, 20, 30, 40]
print(myenumerate(a))


def mymax(*args):
    temp = float('-inf') # присваивание минус бесконечности
    for i in args:
        if i > temp:
            temp = i
    return temp


print("Поиск максимального числа")
print(mymax(1, 2, 3, 7, 21, 3, 0, 55, -12))
