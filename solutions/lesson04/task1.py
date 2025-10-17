def is_arithmetic_progression(lst: list[list[int]]) -> bool:
    n = len(lst)

    if n < 2:
        return True

    a_1, a_n = min(lst), max(lst)
    d = (a_n - a_1) / (n - 1)

    if d % 1 != 0:
        return False

    result = sorted(lst)

    for i in range(n):
        if (a_1 + i * d) in result:
            return True

    return False
