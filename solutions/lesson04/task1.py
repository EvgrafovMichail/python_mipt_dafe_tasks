def is_arithmetic_progression(lst: list[int]) -> bool:
    lst.sort()
    for i in range(len(lst) - 2):
        if lst[i] - lst[i + 1] != lst[i + 1] - lst[i + 2]:
            return False
    return True
