# Написать программу, которая уничтожает файлы и папки по истечении заданного времени. Вы указываете при запуске
# программы путь до папки, за которой нашему скрипту необходимо следить. После запуска программа не должна прекращать
# работать, пока вы не остановите ее работу с помощью Ctrl+C (подсказка: для постоянной работы программы необходим
# вечный цикл, например, "while True:", при нажатии Ctrl+C автоматически остановится любая программа).
# Программа следит за объектами внутри указанной при запуске папки и удаляет их тогда, когда время их существования
# становится больше одной минуты для файлов и больше двух минуты для папок (то есть дата создания отличается от
# текущего момента времени больше чем на одну/две минуты). Ваш скрипт должен смотреть вглубь указанной папки.
# Например, если пользователь создаст внутри нее папку, внутри нее еще одну, а внутри этой какой-то файл,
# то этот файл должен удалиться первым (так как файлу положено жить только одну минуту, а папкам две).
# Вам понадобятся библиотеки os и shutil.
import os as _os
import shutil as _shutil
import time as _time


def time_creation(path_to_file):
    # Вынес в отдельную функцию, так как на разных ОС разные методы получения метки времени файла\папки
    # И в будущем возможно понадобиться реализация варианта под Linux или MAC
    return _os.path.getctime(path_to_file)


def deleter(control_path):
    if _os.path.exists(control_path):
        out_str = list(_os.walk(control_path))
        for path, folders, files in out_str:
            for folder in folders:
                temp_path = _os.path.join(path, folder)
                if (_time.time() - time_creation(temp_path)) > 120:
                    print(f"Folder {temp_path} will be deleted")
                    _shutil.rmtree(temp_path)
            for file in files:
                temp_path = _os.path.join(path, file)
                if (_time.time() - time_creation(temp_path)) > 60:
                    print(f"File {temp_path} will be deleted ")
                    _os.remove(temp_path)
        return True
    else:
        print(f"Folder {control_path} is not exist")
        return False


if __name__ == "__main__":
    work_path = r"E:\GIT_Python\PythonCourseATIS\Practice\a.belyantsev\i"
    flag = True
    while flag:
        flag = deleter(work_path)
