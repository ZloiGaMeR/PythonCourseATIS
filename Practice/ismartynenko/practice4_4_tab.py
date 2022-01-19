def tab2spaces(swt):
    return swt.expandtabs(tabsize=4)


def spaces2tabs(sws):
    return sws.replace("    ", "\t")


# работа со строкой
stroka = "\tHello.\t-\tHi!\t"
print(tab2spaces(stroka))
print(spaces2tabs(stroka))

# работа с файлом
fo = open("practice4_4_tab.txt")
stroka2 = fo.readline()
str_file1 = tab2spaces(stroka2)
print(str_file1)
str_file2 = spaces2tabs(str_file1)
print(str_file2)
fo.close()
