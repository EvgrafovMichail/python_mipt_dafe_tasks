def get_cube_root(n: float, eps: float) -> float:
    sign = 1
    if n < 0:
        n = abs(n)
        sign = -1

    root = n / 2

    while abs(root**3 - n) >= eps:
        if root**3 > n:
            root = root / 2
        elif root**3 < n:
            root = root * 1.5

    return root * sign
