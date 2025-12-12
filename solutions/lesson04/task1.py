def is_arithmetic_progression(lst: list[list[int]]) -> bool:
    # ваш код
    if len(lst) <= 1:
        return True
    list2 = sorted(lst)
    step = list2[1] - list2[0]
    for i in range(len(list2) - 1):
        real_step = list2[i + 1] - list2[i]
        if real_step != step:
            return False

    return True
