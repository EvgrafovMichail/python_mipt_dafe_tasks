def get_cube_root(n: float, eps: float) -> float:
    if n == 0:
        return 0.0
    if n > 0: 
        left = 0.0
        right = max (1.0, n)
    else:
        left = min (-1.0, n)
        right = 0.0 
    while right - left > eps:
        mid = (left + right) / 2
        mid_cub = mid * mid * mid
        
    if mid_cub < n:
        left = mid
    else:
         right = mid
    n =  (left + right) / 2
    return n
