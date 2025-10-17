def is_arithmetic_progression(lst: list[list[int]]) -> bool:
    lst.sort()
    if len(lst) > 2:
        for i in range(len(lst) - 2):
            if abs(lst[i + 1] - lst[i]) != abs(lst[i + 2] - lst[i + 1]):
                return False
    return True
