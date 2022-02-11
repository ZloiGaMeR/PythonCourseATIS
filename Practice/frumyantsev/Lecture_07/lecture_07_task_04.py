import os
import time


my_pth = '.\\TempFolder1'

# lst_dirs.append(path)
# print(lst_dirs)


def path_collector(pth):
    """
    Collects paths of all containing files and folders.
    Returns list of file paths and list of folder paths.
    """
    if not os.path.exists(my_pth):
        print(f"The path does not exist")
        return [], []
    lst_files = []
    lst_dirs = [pth]
    try:
        for file_tup in os.walk(pth):
            print(file_tup)
            lst_files.append(os.path.join(str(file_tup[0]), str(file_tup[2][0])))
            lst_dirs.append(os.path.join(str(file_tup[0]), str(file_tup[1][0])))
    except IndexError:
        lst_dirs.reverse()
        return lst_files, lst_dirs


def file_vanisher(lst_files, lst_dirs):
    time.sleep(60)
    for pth in lst_files:
        os.remove(pth)
    time.sleep(60)
    for pth in lst_dirs:
        os.rmdir(pth)

    # curr_time = dt.datetime.now()
    # curr_time_plus_1m = curr_time + dt.timedelta(seconds=10)


if __name__ == '__main__':
    # print(path_collector(my_pth))
    file_vanisher(*path_collector(my_pth))
