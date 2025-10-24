def get_cube_root(n: float, eps: float) -> float:
    if n == 0.0:
        return 0.0

    if n > 0.0:
        left = 0.0
        right = max(1.0, n)
    else:
        left = min(-1.0, n)
        right = 0.0

    max_iters = 2000
    iteration = 0
    while iteration < max_iters:
        mid = (left + right) / 2.0
        mid_3 = mid * mid * mid

        if abs(mid_3 - n) <= eps:
            return mid

        if mid_3 < n:
            left = mid
        else:
            right = mid

        if abs(right - left) <= 1e-15:
            return (left + right) / 2.0

        it += 1

    return (left + right) / 2.0


# print(get_cube_root(float(input("n = ")), float(input("eps = "))))
