def is_arithmetic_progression(lst: list[int]) -> bool:
    if len(lst) < 2:
        return True

    lst_sorted = sorted(lst)

    dif = lst_sorted[1] - lst_sorted[0]
    pre_num = lst_sorted[1]
    for now_num in lst_sorted[2:]:
        if now_num - pre_num != dif:
            return False
        pre_num = now_num

    return True
