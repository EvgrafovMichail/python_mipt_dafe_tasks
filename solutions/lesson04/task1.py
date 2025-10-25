def is_arithmetic_progression(lst: list[int]) -> bool:
    if not lst or len(lst) == 1:
        return True
    lst = sorted(lst)
    distance = lst[1] - lst[0]
    for i in range(len(lst) - 1):
        if lst[i + 1] - lst[i] != distance:
            return False
    return True
