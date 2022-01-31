# Реализовать функциональность, которая бы “сворачивала” и “разворачивала” символы табуляции в файле или строке.
# То есть, передается на вход файл или строка, необходимо заменить все символы табуляции на четыре пробела,
# либо же заменить все комбинации из четырех символов пробела на символ табуляции.
def replacement(a, isfile, flag):
    if isfile:
        with open(a, "r+") as f:
            text = f.read()
    else:
        text = a
    if flag:
        return text.replace("\t", "    ")
    else:
        return text.replace("    ", "\t")


in_str = "    Привет    мир    "
print(replacement("testfile.txt", True, True))
print(replacement(in_str, False, False))
