# Написать функцию find_primes(end, start), которая ищет все простые числа в диапазоне от заданного числа start
# (по умолчанию 3) до заданного числа end. Далее необходимо:
# Запустить ее три раза последовательно в диапазоне от 3 до 10000, от 10001 до 20000, от 20001 до 30000.
# Запустить ее три раза с теми же аргументами, но каждый раз в отдельном потоке с помощью threading.Thread.
# Что будет, если 'забыть' выполнить start или join для потоков?
# Запустить ее три раза с теми же аргументами, но каждый раз в отдельном процессе с помощью multiprocessing.Process.
# Что будет, если 'забыть' выполнить start или join для процессов?
# Замерить время исполнения каждого варианта, и сравнить результаты.
from math import sqrt
import time
from threading import Thread
import multiprocessing as mp


def is_prime(n):
    if n <= 1:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False

    i = 3
    sqrt_n = sqrt(n)
    while i <= sqrt_n:
        if n % i == 0:
            return False
        i = i + 2
    return True


def find_primes(end, start=3):
    while start < end:
        if is_prime(start):
            print(start, end=";")
        start += 1


if __name__ == '__main__':
    args = [(10000, 3), (20000, 10003), (30000, 20001)]
    print("Simple start")
    enter_time = time.time_ns()
    for arg in args:
        find_primes(arg[0], arg[1])
    exit_time1 = time.time_ns() - enter_time
    print("\nSimple end")
    print("Thread start")
    thread = []
    enter_time = time.time_ns()
    for arg in args:
        t = Thread(target=find_primes, args=arg)
        t.start()
        thread.append(t)
    for t in thread:
        t.join()
    exit_time2 = time.time_ns() - enter_time
    print("\nThread end")
    print("Process start")
    enter_time = time.time_ns()
    process = []
    for arg in args:
        p = mp.Process(target=find_primes, args=arg)
        p.start()
        process.append(p)
    for p in process:
        p.join()
    exit_time3 = time.time_ns() - enter_time
    print("\nProcess end")
    print(f"Simple start: {exit_time1 / 1000000000} sec. \n"
          f"Thread:       {exit_time2 / 1000000000} sec. \n"
          f"Process:      {exit_time3 / 1000000000} sec.")


#  Резюме: Распараллеливание процессов или потоков в математических операциях приводит к увеличению времени исполнения
#  программы. При этом в многопоточности наблюдается одновременный вывод результата с разных потоков
#  (возможно из-за моей кривой реализации)))).
#  В случае если забыть вызвать start() для потока или процесса то поток или процесс будет создан,
#  но не запустится. В случае если забыть вызвать join() для потока или процесса, то программы не будет дожидаться
#  результата выполнения функционала переданного в поток или процесс.
