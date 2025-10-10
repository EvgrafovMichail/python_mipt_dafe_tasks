def get_cube_root(n: float, eps: float) -> float:
    if abs(n) >= 1:
        left = 0
        right = n
    else:
        left = n
        right = 1
    x = n

    while abs(x * x * x - n) > eps:
        x = (left + right) / 2
        if abs(x * x * x) > abs(n):
            right = x
        else:
            left = x

    return x
