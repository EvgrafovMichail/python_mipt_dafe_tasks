def get_cube_root(n: float, eps: float) -> float:
    left, right = (n + 1) * (n > 0), (n - 1) * (n < 0)
    target = n
    n = (left + right) / 2
    while -eps > n * n * n - target or n * n * n - target > eps:
        if target > n * n * n:
            right = n
        else:
            left = n
        n = (left + right) / 2
    return n
