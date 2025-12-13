def is_arithmetic_progression(lst: list[list[int]]) -> bool:
    lst = sorted(lst)

    for i in range(2, len(lst)):
        if lst[i] - lst[i - 1] != lst[i - 1] - lst[i - 2]:
            return False

    return True
