def get_cube_root(n: float, eps: float) -> float:
    x = 0
    if abs(n) >= 1:
        a, b = n / abs(n), n
    else:
        if n == 0:
            return 0
        a, b = 0, n / abs(n)
    while abs(x * x * x - n) > eps / 10:
        x = (b + a) / 2
        if abs(x * x * x) >= abs(n):
            b = x
        else:
            a = x
    return x
