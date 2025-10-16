def is_arithmetic_progression(lst: list[list[int]]) -> bool:
    # ваш код
    if len(lst) < 2:
        return True  # пустой или из 1 элемента — считаем прогрессией
    lst = sorted(lst)
    diff = lst[1] - lst[0]
    for i in range(2, len(lst)):
        if lst[i] - lst[i - 1] != diff:
            return False
    return True
