def get_cube_root(n: float, eps: float) -> float:
    if n == 0:
        return 0

    low = 0
    high = n
    mid = 0

    if n > 1:
        low, high = 0, n
    elif n > 0:
        low, high = 0, 1
    elif n > -1:
        low, high = -1, 0
    else:
        low, high = n, 0

    mid = (low + high) / 2

    while abs(mid * mid * mid - n) > eps:
        mid = (low + high) / 2

        if mid * mid * mid < n:
            low = mid
        else:
            high = mid

    return mid
