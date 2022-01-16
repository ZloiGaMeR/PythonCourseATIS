lst0 = [[9, 2, 7],
        [4, 5, 6],
        [7, 8, 1]]

lst1 = [[9, 2, 3],
        [4, 5, 6],
        [7, 8, 1]]

lst2 = [[1, 4, 5, 0],
        [2, 5, 8, 3]]

lst3 = [[1, 4, 5, 0],
        [2, 6, 8, 6],
        [3, 6, 0, 1]]


def remove_column(numb, lst):

    columns_to_remove = []
    for item in range(len(lst)):
        for subitem in range(len(lst[item])):
            if lst[item][subitem] == numb:
                columns_to_remove.append(subitem)
    columns_to_remove = list(set(columns_to_remove))
    columns_to_remove.sort(reverse=True)

    for col in columns_to_remove:
        for item in range(len(lst)):
            del lst[item][col]
    print(lst)
    return lst


if __name__ == "__main__":
    # remove_column(7, lst0)
    # remove_column(7, lst1)
    # remove_column(2, lst1)
    # remove_column(3, lst2)
    # remove_column(5, lst2)
    # remove_column(6, lst2)
    remove_column(6, lst3)
