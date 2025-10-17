def is_arithmetic_progression(lst: list[list[int]]) -> bool:
    lst_sort = sorted(lst)
    if len(lst) <= 1:
        return True
    a = lst_sort[1] - lst_sort[0]
    for i in range(1, len(lst)):
        if lst_sort[i] - lst_sort[i - 1] != a:
            return False
    return True
