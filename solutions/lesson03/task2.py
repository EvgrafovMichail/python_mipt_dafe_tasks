def get_cube_root(n: float, eps: float) -> float:
    x = 0
    x_min = min(n - 1, 0)
    x_max = n + 1
    while abs((x * x * x) - n) >= eps:
        if x * x * x > n:
            x_max, x = x, (x + x_min) / 2
        else:
            x_min, x = x, (x + x_max) / 2
    return x