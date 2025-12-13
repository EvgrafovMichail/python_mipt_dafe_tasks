def get_cube_root(n: float, eps: float) -> float:
    k = 1
    i = 0
    if n <= 0:
        n *= -1
        k = -1
    a, b, c = 0, 0, 0
    while i * i * i < n:
        i += 1
    c = i
    if i * i * i == n:
        return i * k
    a = i - 1
    b = (a + c) / 2
    while abs((b * b * b) - n) > eps:
        if (b * b * b) < n:
            a = b
            b = (a + c) / 2
        else:
            c = b
            b = (a + c) / 2
    return b * k
