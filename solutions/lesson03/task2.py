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

    while high - low > eps * eps * eps:
        middle = (high + low) / 2
        cube = middle * middle * middle
        if cube > n:
            high = middle
        elif cube < n:
            low = middle
        elif cube == n:
            return middle

    return middle
