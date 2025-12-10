def is_arithmetic_progression(mas: list[list[int]]) -> bool:
    if len(mas) < 2:
        return True

    mas = sorted(mas)
    d = mas[1] - mas[0]

    for x in range(len(mas) - 1):
        if mas[x + 1] - mas[x] == d:
            continue
        else:
            return False
    return True
