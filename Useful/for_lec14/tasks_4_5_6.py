import re


def to_title(str_arg):
    res = list(str_arg)
    i = 0
    while i < len(res):
        if i == 0 or res[i-1] == ' ':
            res[i] = res[i].upper()
        i += 1
    return ''.join(res)


def count_symbol(str_arg, sym):
    count = 0
    for each in str_arg:
        if each == sym:
            count += 1
    return count


def search_ptrn(str_arg):
    flist = []
    new_str = str_arg
    pattern = '\{([0-9|""]*)\}'
    digit_found = False
    empty_found = False
    mobj = re.search(pattern, new_str)
    while mobj:
        if mobj.group(1) == '':
           empty_found = True
        else:
           digit_found = True
        if empty_found and digit_found:
            break
        flist.append(mobj.group(1))
        new_str = re.sub(pattern, '', new_str, 1)
        mobj = re.search(pattern, new_str)
    return flist, digit_found, empty_found


def search_man(str_arg):
    flist = []
    digit_found = False
    empty_found = False
    tmp_str = None
    for each in str_arg:
       if each == '{':
           tmp_str = ''
       elif each == '}':
           if tmp_str == '':
              empty_found = True
           else:
              digit_found = True
           if empty_found and digit_found:
               break
           flist.append(tmp_str)
           tmp_str = None
       elif not tmp_str is None:
           if each.isdigit():
               tmp_str += each
           else:
               tmp_str = None
    return flist, digit_found, empty_found


def myformat(str_arg, *args):
    flist, digit_found, empty_found = search_ptrn(str_arg)
    res_str = str_arg
    if empty_found and digit_found:
        raise ValueError('cannot switch from automatic field numbering to manual field specification')
    elif empty_found:
        i = 0
        pat = re.compile('\{\}')
        while i < len(flist):
            res_str = re.sub(pat, args[i], res_str, 1)
            i += 1
    elif digit_found:
        for each in flist:
            res_str = re.sub('\{' + each + '\}', args[int(each)], res_str)
    return res_str


if __name__ == '__main__':
    a = 'orlov Ilya evgenyevich'
    #print('to_title "{}": {}'.format(a, to_title(a)))
    #print('count_symbol "o": {}'.format(count_symbol(a, 'o')))
    print("myformat('{{1}}, {{0}}, {{2}}', 'a', 'b', 'c'): {}".
          format(myformat('{1}, {0}, {2}', 'a', 'b', 'c')))
    print("myformat('{{}}, {{}}, {{}}', 'a', 'b', 'c'): {}".
          format(myformat('{}, {}, {}', 'a', 'b', 'c')))
    print("myformat(' 1 2 3 ', 'a', 'b'): {}".
          format(myformat(' 1 2 3 ', 'a', 'b')))
    try:
        print("myformat('{{1}}, {{0}}, {{}}', 'a', 'b'): {}".
              format(myformat('{1}, {0}, {}', 'a', 'b')))
    except ValueError as e:
        print('{}: {}'.format(type(e).__name__, e))
    try:
        print("myformat('{{1}}, {{0}}, {{2}}', 'a', 'b'): {}".
              format(myformat('{1}, {0}, {2}', 'a', 'b')))
    except IndexError as e:
        print('{}: {}'.format(type(e).__name__, e))
