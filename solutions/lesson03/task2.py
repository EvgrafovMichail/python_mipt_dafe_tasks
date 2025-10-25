def get_cube_root(n: float, eps: float) -> float:
    x = n / 2
    if n >= 0:
        min_x, max_x = 0, max(1, n)
    else:
        min_x, max_x = min(-1, n), 0
    while abs(x * x * x - n) >= eps:
        x = (min_x + max_x) / 2
        if x * x * x > n:
            max_x = x
        else:
            min_x = x
        min_x, max_x = min(max_x, min_x), max(max_x, min_x)
    return x
