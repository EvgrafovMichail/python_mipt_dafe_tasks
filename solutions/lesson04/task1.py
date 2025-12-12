def is_arithmetic_progression(lst: list[list[int]]) -> bool:
    lst.sort(reverse=True)
    for i in range(0, len(lst) - 2):
        if lst[i] - lst[i + 1] != lst[i + 1] - lst[i + 2]:
            return False
    return True
