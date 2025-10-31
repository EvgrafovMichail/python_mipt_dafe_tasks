def is_arithmetic_progression(lst: list[list[int]]) -> bool:
    n = len(lst)
    for i in range(n - 1):
        for j in range(n - i - 1):
            if lst[j] > lst[j + 1]:
                lst[j], lst[j + 1] = lst[j + 1], lst[j]

    for i in range(0, len(lst) - 2):
        print(abs(lst[i] - lst[i + 1]), abs(lst[i + 1] - lst[i + 2]))
        if abs(lst[i] - lst[i + 1]) == abs(lst[i + 1] - lst[i + 2]):
            continue
        else:
            return False

    return True
