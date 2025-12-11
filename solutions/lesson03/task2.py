def get_cube_root(n: float, eps: float) -> float:
    # ваш код
    abs_n = abs(n)
    middle = 0
    right_border = abs_n
    left_border = 1

    if n == 0:
        return n

    if abs_n > 0 and abs_n < 1:
        left_border = abs_n
        right_border = 1

    while abs((middle * middle * middle) - abs_n) >= eps:
        middle = (right_border + left_border) / 2
        if (middle * middle * middle) > abs_n:
            right_border = middle
        else:
            left_border = middle

    if n < 0:
        n = -middle
    else:
        n = middle

    return n
