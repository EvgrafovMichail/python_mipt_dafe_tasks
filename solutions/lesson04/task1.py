def is_arithmetic_progression(lst: list[list[int]]) -> bool:
    lst.sort()
    i = 0
    if len(lst) <= 2:
        return True
    if len(lst) >= 2:
        while i + 2 < len(lst):
            dif_1 = lst[i + 1] - lst[i]
            dif_2 = lst[i + 2] - lst[i + 1]
            if dif_1 != dif_2:
                return False
            i += 1
    return True
