# Написать генератор для построчного чтения файла

def reader_line(a):
    with open(a, 'r') as f:
        for i in f:
            yield i


for line in reader_line("lec7_text.txt"):
    print(line, end="")
