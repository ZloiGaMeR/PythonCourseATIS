from exam_7 import copy_file
import os.path


def copydir(src, dst):
    for i in os.walk(src):
        path = str(i[0]).replace(os.path.dirname(src), dst)
        os.mkdir(path)
        for j in i[2]:
            src_temp = os.path.join(i[0], j)
            dsc_temp = os.path.join(path, j)
            copy_file(src_temp, dsc_temp)


source = r"C:\Users\dfyz\PycharmProjects\PythonCourseATIS\Practice\ismartynenko"
destination = r"C:\Users\dfyz\Desktop"
copydir(source, destination)
