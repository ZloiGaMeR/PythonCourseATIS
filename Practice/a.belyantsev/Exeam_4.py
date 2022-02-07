import re
import os
import shutil
# Написать реализацию функции range: она может принимать от одного до трех аргументов,
# при этом аргументами должны быть целые числа (int). range(старт, стоп, шаг) - так выглядит стандартный вызов функции range() в Python.
# По умолчанию старт равняется нулю, шаг - единице. Возвращает список целых чисел в форме [старт, старт + шаг, старт + шаг * 2...].
# Если шаг положительное число, последним элементом списка будет наибольшее (старт + i * шаг) меньшее числа стоп.
# Если шаг отрицательное число, то последний элемент будет наименьшее (старт + i * шаг) большее числа стоп.
# Предусмотреть случаи ошибочных аргументов (например, шаг == 0). (5 баллов)


def myrange(start, stop, step):
    if start is None:
        start = 0

    if step is None:
        step = 1

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


print(myrange(9, -10, -2))

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


def copydir(source, destination):
    if os.path.exists(source) and os.path.exists(destination):
        file_list = os.listdir(source)
        for file in file_list:
            shutil.copyfile(os.path.join(source, file), os.path.join(destination, file))
        print("Ready!")
    else:
        print(f"source: {source} or destination: {destination} is not exist")


copydir(r"E:\GIT_Python\PythonCourseATIS\Practice\a.belyantsev\out",
        r"E:\GIT_Python\PythonCourseATIS\Practice\a.belyantsev\in")
