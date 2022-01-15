import datetime


def whitespace_switch(string_or_file):
    """
    “Сворачивает” и “разворачивает” символы табуляции в файле или строке (заменяет все символы табуляции на четыре
    пробела, либо заменяет все комбинации из четырех символов пробела на символ табуляции).
    """
    print("\n")

    try:
        initial_file = open(string_or_file, "r")
        print("Найден файл:")
        date_to_insert_into_file_name = str(datetime.datetime.today())[:19].replace(" ", "_").replace(":", "-")
        name_of_new_output_file = "output_file_created_on_"+date_to_insert_into_file_name+"_based_on"+initial_file.name+".txt"
        output_file = open(name_of_new_output_file, "w")
        line = initial_file.readline()
        new_line = ""
        if line.find(" " * 4) == line.find("\t") == -1:
            print(rf"{line}")
            print("Результат: переданный файл не содержит символов табуляции или четырех пробелов подряд")
        elif line.find("\t") == -1 or line.find(" " * 4) < line.find("\t"):
            new_line = line.replace(" " * 4, "\t")
            print("%r" % new_line)
            print(f"Результат: каждые четыре пробела подряд в переданном файле были заменены "
                  f"на символы табуляции и сохранены в {name_of_new_output_file}")
        elif line.find(" " * 4) == -1 or line.find("\t") < line.find(" " * 4):
            new_line = line.replace("\t", " " * 4)
            print("%r" % new_line)
            print(f"Результат: каждый символ табуляции в переданном файле был заменен "
                  f"на четыре пробела подряд и сохранен в {name_of_new_output_file}")
        output_file.write(new_line)
        initial_file.close()
        output_file.close()
        print('-' * 30)
    except IOError:
        print("Файл не найден\n")
        print(f"Найдена строка: \n\"{string_or_file}\"")
        print("Расположение первого символа табуляции: ", string_or_file.find("\t"))
        print("Расположение первых четырех пробелов подряд: ", string_or_file.find(" " * 4))
        if string_or_file.find("\t") == -1 and string_or_file.find(" " * 4) == -1:
            print(rf"{string_or_file}")
            print("Результат : переданная строка не содержит символов табуляции или четырех пробелов подряд")
        elif string_or_file.find("\t") == -1 or string_or_file.find(" "*4) < string_or_file.find("\t"):
            new_string = string_or_file.replace(" "*4, "\t")
            print("\nРезультат преобразования: \n\"%r\"" % new_string)
            print("(каждые четыре пробела подряд в переданной строке были заменены на символы табуляции)")
        else:#elif string_or_file.find(" " * 4) == -1 or string_or_file.find("\t") < string_or_file.find(" "*4):
            new_string = string_or_file.replace("\t", " "*4)
            print("\nРезультат преобразования: \n\"%r\"" % new_string)
            print("(каждый символ табуляции в переданной строке был заменен на четыре пробела подряд)")
        print('-' * 30)


if __name__ == "__main__":

    str1 = "здесь нет ни четырех пробелов подряд, ни табуляции"
    str2 = "здесь нет    символа табуляции, но есть четыре пробела    подряд"
    str3 = "здесь четыре    пробела\t расположены раньше символа    табуляции"
    str4 = "\tздесь нет четырехпробелов подряд но есть\tсимволы табуляции"
    str5 = "\tздесь\t\t символ табуляции \r расположен раньше    четырех пробелов\t"

    file0 = "lecture_04_task_04_initial_test_file_00"
    file1 = "lecture_04_task_04_initial_test_file_01"
    file2 = "lecture_04_task_04_initial_test_file_02"
    file3 = "lecture_04_task_04_initial_test_file_03"

    whitespace_switch(str1)
    whitespace_switch(str2)
    whitespace_switch(str3)
    whitespace_switch(str4) # failed строка содержит ТОЛЬКО символы табуляции, и интерпретатор,
    # похоже, преобразует их все в четыре пробела
    whitespace_switch(str5) # строка ОДНОВРЕМЕННО содержит символы табуляции и 4 пробела подряд, предположительно
    # поэтому, интерпретатор, не преобразует здесь табуляцию в 4 пробела

    whitespace_switch(file0)
    whitespace_switch(file1)
    whitespace_switch(file2)
    whitespace_switch(file3)
