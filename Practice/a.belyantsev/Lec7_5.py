#  Используя модуль re, найти все команды Git с аргументами в файле Practice/README.md
import re as _re
with open("E:\GIT_Python\PythonCourseATIS\Practice\README.md", "r") as f:
    text_file = f.read()
    regexp = _re.compile(r'git [-:/.@A-z ]+')
    print(_re.findall(regexp, text_file))
