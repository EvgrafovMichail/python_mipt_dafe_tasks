def get_cube_root(n: float, eps: float) -> float:
    if n == 0:
        return 0.0

    sign = 1 if n > 0 else -1
    n = abs(n)

    left, right = (0, n) if n >= 1 else (0, 1)

    while True:
        mid = (left + right) / 2
        cube = mid * mid * mid
        diff = cube - n

        if abs(diff) <= eps:
            return sign * mid

        if diff < 0:
            left = mid
        else:
            right = mid
