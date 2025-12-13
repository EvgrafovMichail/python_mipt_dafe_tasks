def is_arithmetic_progression(lst: list[list[int]]) -> bool:
    if len(lst) == 0 or len(lst) == 1 or len(lst) == 2:
        return True
    else:
        lstSORT = sorted(lst)
        i = 1
        step = lstSORT[1] - lstSORT[0]
        while i < len(lstSORT) - 1:
            if abs(lstSORT[i + 1]) - abs(lstSORT[i]) != step:
                return False
            i += 1
    return True
