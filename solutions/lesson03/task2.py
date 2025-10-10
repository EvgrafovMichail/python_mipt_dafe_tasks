def get_cube_root(n: float, eps: float) -> float:
    if n == 0.0:
        return 0.0

    if n > 1.0:
        left, right = 0.0, n
    elif 0.0 < n <= 1.0:
        left, right = 0.0, 1.0
    elif n < -1.0:
        left, right = n, 0.0
    else:
        left, right = -1.0, 0.0

    max_iter = 2000
    mid = 0.0
    for _ in range(max_iter):
        mid = (left + right) / 2.0
        cube = mid * mid * mid
        if abs(cube - n) <= eps:
            return mid
        if cube < n:
            left = mid
        else:
            right = mid
    n = mid
    return n
