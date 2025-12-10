def is_arithmetic_progression(lst: list[list[int]]) -> bool:
    lst = sorted(lst)

    progression = True

    if len(lst) > 2:
        for i in range(2, len(lst)):
            if lst[i] - lst[i - 1] != lst[i - 1] - lst[i - 2]:
                progression = False
                break

    return progression
