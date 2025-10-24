def get_cube_root(n: float, eps: float) -> float:
    if abs(n) < 1:
        L, R = -1, 1
    elif n > 0:
        L, R = 0, n
    else:
        L, R = n, 0

    while R - L > eps:
        middle = (L + R) / 2
        middle3 = middle * middle * middle

        if middle3 < n:
            L = middle
        else:
            R = middle

    return (L + R) / 2
