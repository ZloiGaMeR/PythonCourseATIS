def sorted_list(a):

    # Create dictionary - d[element] = num
    d = {i: a.count(i) for i in a}

    # Create list keys from dictionary
    lst_final = list(d)

    # Sort list by dictionary values
    lst_final.sort(key=lambda x: d[x])

    return lst_final


lst = [r'wefwr', '3_dd', '1_w', 'wefwr', '2_23', '3_dd', '4', 'wefwr',
       'wefwr', 'wefwr', '2_23', '3_dd', '4', '4', '4', 'unic']

fun = sorted_list(lst)
print(fun)
