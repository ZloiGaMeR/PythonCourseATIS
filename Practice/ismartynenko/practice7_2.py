from subprocess import Popen, PIPE


def func(name):
    cmd = "type " + name
    proc = Popen(cmd, shell=True, stdout=PIPE, stderr=PIPE)
    proc.wait()
    res = proc.communicate()
    return res[0].decode('cp866')


print(func("practice7_1.py"))
