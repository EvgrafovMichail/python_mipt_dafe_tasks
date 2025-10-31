def get_cube_root(n: float, eps: float) -> float:
    if n < 0:
        return -get_cube_root(-n, eps)
    if n >= 1:
        low_border, high_border = 0, n
    else:
        low_border, high_border = 0, 1
    while (
        abs(
            ((low_border + high_border) / 2)
            * ((low_border + high_border) / 2)
            * ((low_border + high_border) / 2)
            - n
        )
        >= eps
    ):
        mid = (low_border + high_border) / 2
        mid_cube = mid * mid * mid
        if mid_cube < n:
            low_border = mid
        else:
            high_border = mid
    return (low_border + high_border) / 2
