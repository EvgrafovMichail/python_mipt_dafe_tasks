def is_arithmetic_progression(lst: list[int]) -> bool:
    if len(lst) < 2:
        return True

    lst.sort()
    d = lst[1] - lst[0]
    for i in range(len(lst) - 1):
        sub = lst[i + 1] - lst[i]
        if sub != d:
            return False
        d = sub
    return True
