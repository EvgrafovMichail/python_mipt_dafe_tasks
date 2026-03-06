def get_cube_root(n: float, eps: float) -> float:
    if n == 0:
        return 0

    if n > 0:
        low = 0.0
        if n >= 1:
            high = n
        else:
            high = 1
    else:
        high = 0
        if n <= -1:
            low = n
        else:
            low = -1

    for i in range(2000):
        mid = (low + high) / 2
        mid_3 = mid * mid * mid

        if abs(mid_3 - n) <= eps:
            return mid

        if mid_3 < n:
            low = mid
        else:
            high = mid

    return (low + high) / 2
