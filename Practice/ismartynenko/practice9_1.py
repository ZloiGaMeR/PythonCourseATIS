import time
import threading
import multiprocessing


'''В случае с потоками и процессами без метода start функция не начнет выполняться
С методом join обстоит иначе, в потоках начинается некорректная работа, то два из 3-ех отработает, то один.
Процессы же не замечают если забыть указать join'''


def find_primes(end, start=3):
    simple_nums = []
    while start <= end:
        i = 2
        j = 0
        while i*i <= start and j != 1:
            if start % i == 0:
                j = 1
                i += 1
            else:
                i += 1
        if j != 1:
            simple_nums.append(start)
        start += 1
    # print(simple_nums)


if __name__ == '__main__':
    print("One thread:", end=' ')
    t_start = time.perf_counter()
    find_primes(10000)
    find_primes(20000, 10001)
    find_primes(30000, 20001)
    print(time.perf_counter() - t_start)

    print("Threads:", end=' ')
    t_start = time.perf_counter()
    th1 = threading.Thread(target=find_primes, args=(10000,))
    th2 = threading.Thread(target=find_primes, args=(20000, 10001))
    th3 = threading.Thread(target=find_primes, args=(30000, 20001))
    th1.start()
    th2.start()
    th3.start()
    th1.join()
    th2.join()
    th3.join()
    print(time.perf_counter() - t_start)

    print("Processes:", end=' ')
    t_start = time.perf_counter()
    mp1 = multiprocessing.Process(target=find_primes, args=(10000,))
    mp2 = multiprocessing.Process(target=find_primes, args=(20000, 10001))
    mp3 = multiprocessing.Process(target=find_primes, args=(30000, 20001))
    mp1.start()
    mp2.start()
    mp3.start()
    mp1.join()
    mp2.join()
    mp3.join()
    print(time.perf_counter() - t_start)
