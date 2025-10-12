def get_cube_root(n: float, eps: float) -> float:
    if n == 0:
        return 0.0

    if n > 0:
        left = 0
        right = max(1, abs(n))
    else:
        left = min(-1, -abs(n))
        right = 0

    while right**3 - left**3 >= eps:
        x = (left + right) / 2
        x_cube = x**3

        if x_cube > n:
            right = x
        else:
            left = x
    return (left + right) / 2