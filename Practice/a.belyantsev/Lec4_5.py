# Интерполировать некие шаблоны в строке: есть строка с определенного вида форматированием,
# необходимо заменить в этой строке все вхождения шаблонов на их значение из словаря.
str = "sdsf fdfsd refsdf w fsgsd wefvcxvsdfv"
dictionary = {"sdsf": "абвы"}

for key, value in dictionary.items():
    str = str.replace(key, value)
print(str)
