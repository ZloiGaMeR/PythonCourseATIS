def selection_sort(lst: list):
    """
    Выполняет алгоритм сортировки выбором.Меняет первый элемент в списке с минимальным
    из последующих, затем второй элемент в списке с минимальным из последующих и т. д.
    """
    for i in range(len(lst)-1):
        lst[i], lst[lst.index(min(lst[i+1:]), i+1)] = lst[lst.index(min(lst[i + 1:]), i + 1)], lst[i]
    print(lst)
    return lst


if __name__ == "__main__":
    selection_sort([3, 24, 2, 3, 0, 7])
    selection_sort([-5, 21, 34, 3, 24, -12, 2, 3, 10, 73, -30])
