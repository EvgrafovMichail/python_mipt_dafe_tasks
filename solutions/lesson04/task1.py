def is_arithmetic_progression(lst: list[list[int]]) -> bool:
    if len(lst) == 1:
        return True
    if lst == []:
        return True
    lst.sort()
    d = lst[1] - lst[0]

    for i in range(0, len(lst) - 1):
        if lst[i + 1] - lst[i] != d:
            return False

    return True
