def is_arithmetic_progression(lst: list[list[int]]) -> bool:
    temp = 0
    for i in range(0, len(lst)):
        for j in range(i + 1, len(lst)):
            if lst[i] < lst[j]:
                temp = lst[i]
                lst[i] = lst[j]
                lst[j] = temp

    for i in range(0, len(lst) - 2):
        if lst[i] - lst[i + 1] != lst[i + 1] - lst[i + 2]:
            return False
    return True
