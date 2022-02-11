import re
import os
import shutil
# Написать реализацию функции range: она может принимать от одного до трех аргументов,
# при этом аргументами должны быть целые числа (int). range(старт, стоп, шаг) - так выглядит стандартный вызов функции range() в Python.
# По умолчанию старт равняется нулю, шаг - единице. Возвращает список целых чисел в форме [старт, старт + шаг, старт + шаг * 2...].
# Если шаг положительное число, последним элементом списка будет наибольшее (старт + i * шаг) меньшее числа стоп.
# Если шаг отрицательное число, то последний элемент будет наименьшее (старт + i * шаг) большее числа стоп.
# Предусмотреть случаи ошибочных аргументов (например, шаг == 0). (5 баллов)


def myrange(*args):
    if len(args) == 2:
        start = 0
        stop = args[0]
        step = args[1]
    elif len(args) == 3:
        start = args[0]
        stop = args[1]
        step = args[2]
    else:
        print("Arguments are not correct")
        return None

    out = []
    i = 0
    if step == 0:
        print("Step should not be 0")
        return None
    if step > 0:
        cmp = lambda x: x < stop
    else:
        cmp = lambda x: x > stop
    while cmp(start + i * step):
        out.append(start + i * step)
        i += 1
    return out


print(myrange(1, 10, -1))
print(myrange())
print(myrange(10, 0))
print(myrange(9, -10, -1))

# Написать реализацию функции format. (5 баллов, с re – 7 баллов)
#
# >>> myformat('{1}, {0}, {2}', 'a', 'b', 'c')
# 'b, a, c'
# >>> myformat('coordinates: {}, {}', '37.4N', '18.3W')
# 'coordinates: 37.4N, 18.3W'


def myformat(out_str, *args):
    i = 0
    while i < len(args):
        regexp = '{' + str(i) + '?' + '}'
        out_str = re.sub(regexp, args[i], out_str, 1)
        i += 1
    return out_str


print(myformat('coordinates: {}, {}', '37.4N', '18.3W'))
print(myformat('{1}, {0}, {2}', 'a', 'b', 'c'))


# Написать функцию copydir - копирование директории с использованием copyfile,
# а также проверки на существование source и destination. (5 баллов)

def copyfile(source, destination):
    with open(source, "r") as read_f, open(destination, "x") as write_f:
        write_f.write(read_f.read())


def copydir(source, destination):
    if os.path.exists(source) and os.path.exists(destination):
        for file in os.listdir(source):
            temp_source = os.path.join(source, file)
            temp_destination = os.path.join(destination, file)
            if os.path.isdir(temp_source):
                os.makedirs(temp_destination)
                copydir(temp_source, temp_destination)
            else:
                copyfile(temp_source, temp_destination)
        print("Ready!")
    else:
        print(f"source: {source} or destination: {destination} is not exist")


copydir(r"E:\GIT_Python\PythonCourseATIS\Practice\a.belyantsev\out",
        r"E:\GIT_Python\PythonCourseATIS\Practice\a.belyantsev\in")
