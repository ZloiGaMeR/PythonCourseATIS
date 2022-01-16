def selection_sort(lst: list):
    """
    Выполняет алгоритм сортировки выбором.Меняет первый элемент в списке с минимальным
    из последующих, затем второй элемент в списке с минимальным из последующих и т. д.
    """
    print(f"Исходный список:\t\t\t{lst}")
    for i in range(len(lst)):
        min_lst_ind = i
        j = i + 1
        while i < j < len(lst):
            if lst[j] < lst[min_lst_ind]:
                min_lst_ind = j
            j += 1
        lst[i], lst[min_lst_ind] = lst[min_lst_ind], lst[i]
    print(f"Отсортированный список:\t\t{lst}")
    return lst


if __name__ == "__main__":
    selection_sort([3, 24, 2, 3, 0, 7])
    selection_sort([-5, 21, 34, 3, 24, -12, 2, 3, 10, 73, -30])
