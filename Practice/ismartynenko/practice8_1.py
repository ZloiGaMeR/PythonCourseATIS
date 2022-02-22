def sorted_list(a):
    d = {}
    d_sort = []

    # Create dictionary - d[element] = num
    for i in a:
        d[i] = a.count(i)

    # Sorting
    while len(d) != 0:
        mini_val = d[lst[0]]
        mini_key = lst[0]
        for i in d.items():
            if i[1] < mini_val:
                mini_val = i[1]
                mini_key = i[0]

        # Add to sorted list and delete from unsorted dictionary
        d_sort.append(mini_key)
        del d[mini_key]
    print(d_sort)


lst = [r'5_wefwr', '3_dd', '1_w', '5_wefwr', '2_23', '3_dd', '4', '5_wefwr',
       '5_wefwr', '5_wefwr', '2_23', '3_dd', '4', '4', '4', 'unic']

sorted_list(lst)
