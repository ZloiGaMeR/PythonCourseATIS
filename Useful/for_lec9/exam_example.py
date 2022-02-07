import os

def fun(src, dst):
    with open(src, 'r') as f_in:
        with open(dst, 'x') as f_out:
            f_out.write(f_in.read())


# try:
#     fun('somefile_in.txt', 'somefile_out.txt')
# except FileNotFoundError as ex:
#     print(f"Файл не найден: {ex}")
# except FileExistsError as ex:
#     print(f"Файл уже существует: {ex}")



def copydir(src, dst):
    os.mkdir(dst)
    for each in os.listdir(src):
        basename = os.path.basename(each)
        if os.path.isfile(each):
            fun(each, os.path.join(dst, basename))
        else:
            copydir(each, os.path.join(dst, basename))


def myrange(start=0, stop=None, step=1):
    if stop is None:
        stop = start
        start = 0

    if step > 0:
        fun = lambda x, y: x < y
    elif step < 0:
        fun = lambda x, y: x > y
    else:
        raise ValueError("myrange() arg 3 must not be zero")

    while fun(start, stop):  # 5, 1, -1
        yield start
        start += step

for i in myrange(1, 5, 0):
    print(i)
