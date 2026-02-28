def is_arithmetic_progression(lst: list[list[int]]) -> bool:
    if len(lst) <= 2:
        return True
    lst = sorted(lst)
    if all((lst[i] - lst[i - 1]) == (lst[i + 1] - lst[i]) for i in range(1, len(lst) - 1)):
        return True
    return False
