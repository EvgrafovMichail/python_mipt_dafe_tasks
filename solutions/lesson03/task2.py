def get_cube_root(n: float, eps: float) -> float:
    if n == 0:
        return 0.0
    
    if n > 0:
        if n < 1:
            left = 0.0
            right = 1.0
        else:
            left = 0.0
            right = max(1.0, n)
    else:
        if n > -1:
            left = -1.0
            right = 0.0
        else:
            left = min(-1.0, n)
            right = 0.0
    
    # Бинарный поиск
    while right - left > eps:
        mid = (left + right) / 2
        mid_3 = mid * mid * mid
        
        if mid_3 < n:
            left = mid
        else:
            right = mid
    
    return (left + right) / 2

#print(get_cube_root(float(input("n = ")), float(input("eps = "))))