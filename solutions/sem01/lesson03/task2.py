def get_cube_root(n: float, eps: float) -> float:
    if n == 0:
        return 0

    abs_n = abs(n)

    low = 0
    high = abs_n if abs_n >= 1 else 1
    mid = (low + high) / 2
    mid3 = mid * mid * mid
    while abs(mid3 - abs_n) > eps:
        if mid3 > abs_n:
            high = mid
        else:
            low = mid

        mid = (low + high) / 2
        mid3 = mid * mid * mid

    return mid * abs_n / n
