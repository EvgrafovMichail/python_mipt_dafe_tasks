def is_arithmetic_progression(lst: list[list[int]]) -> bool:
    lst.sort()
    if len(lst) <= 2:
        return True
    d = lst[1] - lst[0]
    for i in range(1, len(lst)):
        if lst[i] - lst[i-1] != d:
            return False


    return True