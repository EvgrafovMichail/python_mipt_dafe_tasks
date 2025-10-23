def get_cube_root(n: float, eps: float) -> float:
    if abs(n) >= 1:
        left = 0
        right = n
    else:
        left = n
        right = n / abs(n)
    x = n

    while abs(x * x * x - n) > eps:
        x = (left + right) / 2
        if abs(x * x * x) > abs(n):
            right = x
        else:
            left = x

    return x


print(get_cube_root(-0.9, 1e-3))
