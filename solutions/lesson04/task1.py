def is_arithmetic_progression(lst: list[list[int]]) -> bool:
    if len(lst) < 2:
        return True

    lst.sort()

    diff = lst[1] - lst[0]
    for i in range(2, len(lst)):
        if (lst[i] - lst[i - 1]) != diff:
            return False

    return True
