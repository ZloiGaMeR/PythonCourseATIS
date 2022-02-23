def sorted_list(a):
    # Sort list
    # Тут я думал как мне не создавать новый список, но никак не выходило.
    # хотел что то вроде: a.sort(key=lambda x: a.count(x)). Ну ладно,
    # работаем с копией, но тут тогда другой момент
    # почему не могу сделать так: lst_sort.sort(key=lambda x: lst_sort.count(x)) ???
    lst_sort = a.copy()
    lst_sort.sort(key=lambda x: a.count(x))

    # Create dictionary - d[element] = num
    d = {}
    for i in lst_sort:
        d[i] = lst_sort.count(i)

    # Create list
    lst_final = []
    for i in d.keys():
        lst_final.append(i)

    return lst_final


lst = [r'wefwr', '3_dd', '1_w', 'wefwr', '2_23', '3_dd', '4', 'wefwr',
       'wefwr', 'wefwr', '2_23', '3_dd', '4', '4', '4', 'unic']

fun = sorted_list(lst)
print(fun)
