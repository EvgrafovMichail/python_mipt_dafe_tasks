def is_arithmetic_progression(lst: list[list[int]]) -> bool:
    lst.sort()
    if len(lst) == 0:
        return True
    if len(lst) == 1:
        return True
    step = lst[1] - lst[0]
    for i in range(len(lst) - 1):
        if lst[i + 1] - lst[i] != step:
            return False
    return True
