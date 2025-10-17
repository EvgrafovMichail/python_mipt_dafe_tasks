def is_arithmetic_progression(lst: list[list[int]]) -> bool:
    while len(lst) >= 3:
        i1 = (max(lst) - min(lst)) / (len(lst) - 1)
        lst.remove(min(lst))
        i2 = (max(lst) - min(lst)) / (len(lst) - 1)
        if i1 != i2:
            return False
    return True
