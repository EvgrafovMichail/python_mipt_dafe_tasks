def is_arithmetic_progression(lst: list[list[int]]) -> bool:
    # ваш код

    lst.sort()
    if len(lst) >= 2:
        step = lst[1] - lst[0]
        for i in range(1, len(lst) - 1):
            if lst[i + 1] - lst[i] != step:
                return False
        return True
    else:
        return True
