def get_cube_root(n: float, eps: float) -> float:
    if n == 0:
        return 0.0
    if n > 0:
        left = 0.0
        if n > 1:
            right = n
        else:
            right = 1.0
    else:
        right = 0.0
        if n < -1:
            left = n
        else:
            left = -1.0
    ave = (right + left) / 2
    ave_cube = ave * ave * ave
    while abs(ave_cube - n) >= eps:
        if ave_cube > n:
            right = ave
        else:
            left = ave
        ave = (right + left) / 2
        ave_cube = ave * ave * ave
    return (right + left) / 2
