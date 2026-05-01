def get_cube_root(n: float, eps: float) -> float:
    x = 0
    if abs(n) >= 1:
        lt = -abs(n)
        rt = abs(n)
        while abs(x**3 - n) >= eps:
            if x**3 > n:
                rt = x
            else:
                lt = x
            x = (rt + lt) / 2
    else:
        lt = -1
        rt = 1
        while abs(x**3 - n) >= eps:
            if x**3 > n:
                rt = x
            else:
                lt = x
            x = (rt + lt) / 2
    return x
