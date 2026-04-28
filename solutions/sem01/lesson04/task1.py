def is_arithmetic_progression(lst: list[list[int]]) -> bool:
    if len(lst) == 1 or len(lst) == 0:
        return True
    lst.sort()
    k = lst[1] - lst[0]
    for i in range(len(lst) - 1):
        if (lst[i + 1] - lst[i]) != k:
            return False
    return True
