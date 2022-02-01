def gen(fo):
    while True:
        line = fo.readline()
        if not line:
            break
        yield line


with open("practice7_razminka_2.txt", "r") as f:
    for i in gen(f):
        print(i, end="")
