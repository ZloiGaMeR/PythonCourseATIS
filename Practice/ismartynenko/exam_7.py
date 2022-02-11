def copy_file(src, dst):
    try:
        f = open(src, "r")
    except FileNotFoundError:
        print("Source file not found")
        return None

    try:
        fo = open(dst, "x")
    except FileExistsError:
        print("Destination file already exist")
        return None

    fo.write(f.read())


if __name__ == '__main__':
    copy_file("exam.txt", "exam2.txt")
