def sort_by_occurrence(lst):
    '''
    (list) -> list
    Return list containing unique elements sorted by occurrence in original list.
    '''
    dct = {}
    for item in lst:
        if item in dct:
            dct[item] += 1
        else:
            dct[item] = 1
    lst = list(dct.keys())
    lst.sort(key=lambda x: dct[x], reverse=False)
    return lst


if __name__ == '__main__':
    print(sort_by_occurrence([3, 2, 1, 0, 4, 7, 4, 4, 4, 7, 7, 0, -1, 3, 3, 1, 1, 2]))
