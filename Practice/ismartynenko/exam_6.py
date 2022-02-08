import re


def myformat(mystr, *args):
    obj = re.findall(r'{\d}', mystr)
    if len(obj) != 0:
        arr = re.findall(r'\d', mystr)
        for i in range(len(obj)):
            mystr = re.sub(r"{\d}", args[int(arr[i])], mystr, 1)
        print(mystr)
    else:
        obj = re.findall('{}', mystr)
        for i in range(len(obj)):
            mystr = re.sub("{}", args[i], mystr, 1)
        print(mystr)


myformat('{1}, {0}, {2}', 'a', 'b', 'c')
myformat('coordinates: {}, {}', '37.4N', '18.3W')
