# Реализовать запуск функции, осуществляющей операцию сложения для различных типов (integer, string, list)
# параллельно с различными наборами аргументов.
from multiprocessing import Pool


def summ(a, b):
    return a + b


if __name__ == '__main__':
    with Pool(processes=3) as p:
        res = p.starmap(summ, [(1, 2), ("1", "2"), ([1, 2, 3], [4, 5])])
    for value in res:
        print(value)
