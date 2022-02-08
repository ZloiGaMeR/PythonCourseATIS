import re


def myformat(*args):
    mystr = args[0]
    obj = re.findall(r'{\d}', args[0])
    if len(obj) != 0:
        arr = re.findall(r'\d', args[0])
        for i in range(len(obj)):
            mystr = re.sub(r"{\d}", args[int(arr[i])+1], mystr, 1)
        print(mystr)
    else:
        obj = re.findall('{}', args[0])
        for i in range(len(obj)):
            mystr = re.sub("{}", args[i + 1], mystr, 1)
        print(mystr)


myformat('{1}, {0}, {2}', 'a', 'b', 'c')
myformat('coordinates: {}, {}', '37.4N', '18.3W')
