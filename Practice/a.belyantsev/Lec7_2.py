# С помощью библиотеки subprocess прочитать содержимое произвольного файла с использованием утилиты cat в Linux
# или type в Windows (имя файла должно передаваться как параметр в вашу функцию).
from subprocess import Popen, PIPE
import os as _os


def reader(path, name):
    full_path = _os.path.join(path, name)
    proc = Popen(['type', full_path], stdout=PIPE, stderr=PIPE, shell=True)
    proc.wait()
    res = proc.communicate()
    if proc.returncode:
        print(res[1].decode('cp866'))
    return res[0].decode('cp866')


project_path = r"E:\GIT_Python\PythonCourseATIS\Practice\a.belyantsev"
file_name = "testfile.txt"
print(reader(project_path, file_name))
