from exam_7 import copy_file
import os.path


def copydir(src, dst):
    dir_and_files = []
    for i in os.walk(src):
        dir_and_files.append(i)

    src_files = []
    dst_files = []
    for i in dir_and_files:
        path = str(i[0]).replace(os.path.dirname(src), dst)
        os.mkdir(path)
        for j in i[2]:
            src_files.append(os.path.join(i[0], j))
            dst_files.append(os.path.join(path, j))

    for i in range(len(src_files)):
        copy_file(src_files[i], dst_files[i])


source = r"C:\Users\dfyz\PycharmProjects\PythonCourseATIS\Practice\ismartynenko"
destination = r"C:\Users\dfyz\Desktop"
copydir(source, destination)
