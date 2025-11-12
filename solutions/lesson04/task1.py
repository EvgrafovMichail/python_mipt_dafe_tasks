def is_arithmetic_progression(lst: list[list[int]]) -> bool:
    list_sort = sorted(lst)
    if len(list_sort) == 1 or len(list_sort) == 0:
        return True
    delta = list_sort[0] - list_sort[1]
    for i in range(1, len(list_sort) - 1):
        if delta != (list_sort[i] - list_sort[i + 1]):
            return False
    return True
