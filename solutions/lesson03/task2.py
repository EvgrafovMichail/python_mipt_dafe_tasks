def get_cube_root(n: float, eps: float) -> float:
    if n == 0:
        return 0.0

    sign = 1 if n >= 0 else -1
    n_abs = abs(n)
    

    if n_abs >= 1:
        left, right = 0.0, n_abs
    else:
        left, right = 0.0, 1.0
    

    while True:
        mid = (left + right) / 2
        mid_cubed = mid * mid * mid
        
        if abs(mid_cubed - n_abs) <= eps:
            return sign * mid
        
        if mid_cubed < n_abs:
            left = mid
        else:
            right = mid
