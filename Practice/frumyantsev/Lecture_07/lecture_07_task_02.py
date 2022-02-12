from subprocess import Popen, PIPE


def read_file(file):
    fl = Popen(['type', file], stdout=PIPE, stderr=PIPE, shell=True)
    fl.wait()
    res = fl.communicate()  # получить tuple('stdout', 'stderr')
    if fl.returncode:
        print(res[1].decode('cp866'))
    print('result:')
    print(res[0].decode('cp866'))


if __name__ == "__main__":
    # read_file('text0.txt')
    read_file('text1.txt')
    # read_file('text2.txt')
