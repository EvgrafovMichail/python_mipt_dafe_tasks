def is_arithmetic_progression(lst: list[int]) -> bool:
    lst.sort()
    if len(lst) <= 1:
        return True
    d = lst[0] - lst[1]
    for i in range(len(lst) - 1):
        if lst[i] - lst[i + 1] != d:
            return False
    return True
