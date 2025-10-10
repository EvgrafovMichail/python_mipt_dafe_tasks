def get_cube_root(n: float, eps: float) -> float:
    if n == 0:
        return 0

    if n > 0:
        l = 0
        if n >= 1:
            h = n
        else:
            h = 1
    else:
        h = 0
        if n <= -1:
            l = n
        else:
            l = -1

    for i in range(2000):
        mid = (l + h) / 2
        mid_3 = mid * mid * mid

        if abs(mid_3 - n) <= eps:
            return mid

        if mid_3 < n:
            l = mid
        else:
            h = mid

    return (l + h) / 2
