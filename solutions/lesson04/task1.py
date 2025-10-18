def is_arithmetic_progression(lst: list[list[int]]) -> bool:
    a = len(lst)
    if a <= 2:
        return True

    for i in range(2):
        for j in range(a - 1 - i):
            if lst[j] > lst[j + 1]:
                lst[j], lst[j + 1] = lst[j + 1], lst[j]

    for i in range(2, a):
        for j in range(a - 1 - i):
            if lst[j] > lst[j + 1]:
                lst[j], lst[j + 1] = lst[j + 1], lst[j]

        if 2 * lst[-i] != lst[-i - 1] + lst[-i + 1]:
            return False

    return True
