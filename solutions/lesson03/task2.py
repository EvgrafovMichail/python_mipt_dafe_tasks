def get_cube_root(n: float, eps: float) -> float:
    if n < 0:
        n = -n
        r = 0
        while r * r * r < n:
            r += 1
        l = 0
        while r * r * r - n >= eps:
            if ((r + l) * (r + l) * (r + l) / 8 - n) < 0:
                l = (r + l) / 2
            else:
                r = (r + l) / 2

        return -r
    r = 0
    while r * r * r < n:
        r += 1
    l = 0
    while r * r * r - n >= eps:
        if ((r + l) * (r + l) * (r + l) / 8 - n) < 0:
            l = (r + l) / 2
        else:
            r = (r + l) / 2
    return r
