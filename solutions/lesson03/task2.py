def get_cube_root(n: float, eps: float) -> float:
    if eps <= 0:
        print("Ошибка Ввода")
        return None
    if n == 0:
        return 0
    if n > 0:
        low = 0
        high = max(1, n)
    else:
        low = min(-1, n)
        high = 0
    middle = (low + high) / 2
    while abs(n - middle**3) > eps:
        if middle**3 >= n:
            high = middle
        else:
            low = middle
        middle = (low + high) / 2

    return middle

