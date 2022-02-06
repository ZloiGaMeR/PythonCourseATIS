import re
import os
import shutil
# Написать реализацию функции range: она может принимать от одного до трех аргументов,
# при этом аргументами должны быть целые числа (int). range(старт, стоп, шаг) - так выглядит стандартный вызов функции range() в Python.
# По умолчанию старт равняется нулю, шаг - единице. Возвращает список целых чисел в форме [старт, старт + шаг, старт + шаг * 2...].
# Если шаг положительное число, последним элементом списка будет наибольшее (старт + i * шаг) меньшее числа стоп.
# Если шаг отрицательное число, то последний элемент будет наименьшее (старт + i * шаг) большее числа стоп.
# Предусмотреть случаи ошибочных аргументов (например, шаг == 0). (5 баллов)


def myrange(stop, step=1, start=0):
    out = [start, ]
    i = 1
    if step == 0:
        return print("Step should not be 0")
    if step > 0:
        while start + i * step < stop:
            out.append(start + i*step)
            i += 1
        return out
    else:
        while start + i * step > stop:
            out.append(start + i * step)
            i += 1
        return out


print(myrange(-10, -2, 9))

# Написать реализацию функции format. (5 баллов, с re – 7 баллов)
#
# >>> myformat('{1}, {0}, {2}', 'a', 'b', 'c')
# 'b, a, c'
# >>> myformat('coordinates: {}, {}', '37.4N', '18.3W')
# 'coordinates: 37.4N, 18.3W'


def myformat(*args):
    out_str = args[0]
    i = 0
    while i < len(args) - 1:
        regexp = '{' + str(i) + '?' + '}'
        out_str = re.sub(regexp, args[i + 1], out_str, 1)
        i += 1
    return out_str


print(myformat('coordinates: {}, {}', '37.4N', '18.3W'))
print(myformat('{1}, {0}, {2}', 'a', 'b', 'c'))


# Написать функцию copydir - копирование директории с использованием copyfile,
# а также проверки на существование source и destination. (5 баллов)


def copydir(source, destination):
    if os.path.exists(source) and os.path.exists(destination):
        file_list = os.listdir(source)
        for file in file_list:
            shutil.copy(os.path.join(source, file), destination)
        print("Ready!")
    else:
        print(f"source: {source} or destination: {destination} is not exist")


copydir(r"E:\GIT_Python\PythonCourseATIS\Practice\a.belyantsev\out",
        r"E:\GIT_Python\PythonCourseATIS\Practice\a.belyantsev\in")
