def get_cube_root(n: float, eps: float) -> float:
    if n == 0:
        return 0.0
    elif n == 1:
        return 1.0
    elif n == -1:
        return -1.0
    elif n > 1:
        min_sol = 1.0
        max_sol = n
    elif 0 < n < 1:
        min_sol = n
        max_sol = 1.0
    elif -1 < n < 0:
        min_sol = -1.0
        max_sol = 0.0
    elif n < -1:
        min_sol = n
        max_sol = -1.0
    mid_zn = (max_sol + min_sol) / 2
    while True:
        mid_zn = (max_sol + min_sol) / 2
        if abs(mid_zn * mid_zn * mid_zn - n) <= eps:
            n = mid_zn
            break
        if mid_zn * mid_zn * mid_zn > n:
            max_sol = mid_zn
        else:
            min_sol = mid_zn
    return n
