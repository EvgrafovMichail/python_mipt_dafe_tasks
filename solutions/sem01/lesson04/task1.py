def is_arithmetic_progression(lst: list[list[int]]) -> bool:
    lst.sort()
    if len(lst) in [0, 1]:
        return True
    flag = True
    change = lst[1] - lst[0]
    i = 1
    while flag and i < len(lst):
        if lst[i] - lst[i - 1] != change:
            flag = False
        i += 1
    return flag
