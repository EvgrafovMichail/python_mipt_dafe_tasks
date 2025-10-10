def get_cube_root(n: float, eps: float) -> float:
    if n == 1 or n == -1 or n == 0:
        return n
    left = min(0, min(1, n))
    right = max(0, max(1, n))
    while True:
        mid = (right + left) / 2
        if abs(mid * mid * mid - n) < eps:
            break
        if mid * mid * mid < n:
            left = mid
        else:
            right = mid
    return mid