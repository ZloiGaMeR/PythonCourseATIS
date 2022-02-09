import re


def myformat(mystr, *args):
    regexp_c1 = re.compile(r'{\d}')
    regexp_c2 = re.compile(r'{}')

    obj = re.findall(regexp_c1, mystr)
    if len(obj) != 0:
        arr = re.findall(r'\d', mystr)
        for i in range(len(obj)):
            mystr = re.sub(regexp_c1, args[int(arr[i])], mystr, 1)
    else:
        obj = re.findall(regexp_c2, mystr)
        for i in range(len(obj)):
            mystr = re.sub(regexp_c2, args[i], mystr, 1)
    return mystr


print(myformat('{1}, {0}, {2}', 'a', 'b', 'c'))
print(myformat('coordinates: {}, {}', '37.4N', '18.3W'))
