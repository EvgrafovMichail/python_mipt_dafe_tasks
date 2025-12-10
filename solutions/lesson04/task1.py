def is_arithmetic_progression(lst: list[list[int]]) -> bool:
    if len(lst) <= 2:
        return True

    lst_sorted = sorted(lst)
    d = lst_sorted[1] - lst_sorted[0]

    for i in range(2, len(lst_sorted)):
        if lst_sorted[i] - lst_sorted[i - 1] != d:
            return False
    return True
