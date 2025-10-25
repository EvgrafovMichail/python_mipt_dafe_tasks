def is_arithmetic_progression(lst: list[list[int]]) -> bool:
    list_length = len(lst)

    if list_length <= 1:
        return True

    lst.sort()

    delta = lst[1] - lst[0]

    for i in range(1, list_length - 1):
        if lst[i + 1] - lst[i] != delta:
            return False

    return True
