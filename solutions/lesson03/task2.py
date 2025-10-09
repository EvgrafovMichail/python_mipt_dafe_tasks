def get_cube_root(num: float, pogreshnost: float) -> float:
    if num == 0:
        return 0
    if num < 100:
        maxi = 100
    else:
        maxi = num
    flag = False
    if num < 0:
        flag = True
    num = abs(num)
    left = 0.0
    right = 2 + num // 3
    while left < right:
        m = (right + left) / 2
        if abs(num - m * m * m) < pogreshnost:
            if flag:
                return -1 * m
            return m
        elif pogreshnost > num - m * m * m:
            right = m - pogreshnost / maxi
        elif m * m * m - num < pogreshnost:
            left = m + pogreshnost / maxi
