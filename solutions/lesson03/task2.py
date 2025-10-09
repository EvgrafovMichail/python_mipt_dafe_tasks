def get_cube_root(n: float, eps: float) -> float:
    x = n / 2
    while abs(x * x * x - n) >= eps:
        if abs(x * x * x) > abs(n):
            x /= 2
        else:
            x = x * 3 / 2
    return x
