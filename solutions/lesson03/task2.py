def get_cube_root(n: float, eps: float) -> float:
    x = n / 2
    n_abs = n
    while abs(x * x * x - n_abs) >= eps:
        if abs(x * x * x) > abs(n_abs):
            x /= 2
            n /= 2
        else:
            x = x * 5 / 2
    return x
