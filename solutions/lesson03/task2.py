def get_cube_root(n: float, eps: float) -> float:
    if n == 0 or n == 1 or n == -1:
        return n

    if n > 0:
        m = 0
        M = max(n, 1)

    if n < 0:
        m = min(n, -1)
        M = 0

    mid = (m + M) / 2

    while abs(mid * mid * mid - n) > eps:
        if mid * mid * mid < n:
            m = mid
        else:
            M = mid
        mid = (m + M) / 2

    return mid
