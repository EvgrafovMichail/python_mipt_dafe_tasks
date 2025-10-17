def is_arithmetic_progression(lst: list[list[int]]) -> bool:

    lst.sort()
    if len(lst) > 1:

        dif = lst[1] - lst[0]

        for i in range (2, len(lst)):
            if lst[i] - lst[i - 1] != dif:
                return False

    return True