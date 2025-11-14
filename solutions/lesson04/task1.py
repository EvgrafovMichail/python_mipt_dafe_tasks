def is_arithmetic_progression(lst: list[list[int]]) -> bool:
    lst.sort()
    i = 1
    d = 0
    while i < len(lst):
        if i == 1:
            d = lst[i] - lst[i - 1]
        elif lst[i] - lst[i - 1] != d:
            return False

        i += 1

    return True
