def get_cube_root(n: float, eps: float) -> float:
    
    begin, end = -2**32, 2**32
    
    while True:
        mid = (begin + end) / 2
        
        if abs(mid*mid*mid - n) < eps:
            return mid
        
        if mid*mid*mid > n:
            end = mid
        else:
            begin = mid

