def is_arithmetic_progression(lst: list[list[int]]) -> bool:
    lst = sorted(lst)
    ok = True
    for i in range(len(lst)-2):
        if lst[i] - lst[i+1] != lst[i+1] - lst[i+2]:
            ok = False
            break

    return ok
