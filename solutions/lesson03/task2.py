def get_cube_root(n: float, eps: float) -> float:
    if n < 0:
        n = -n
        right = 0
        while right**3 < n:
            right += 1
        left = 0
        while right**3 - n >= eps:
            if ((right + left) ** 3 / 8 - n) < 0:
                left = (right + left) / 2
            else:
                right = (right + left) / 2

        return -right
    right = 0
    while right**3 < n:
        right += 1
    left = 0
    while right**3 - n >= eps:
        if ((right + left) ** 3 / 8 - n) < 0:
            left = (right + left) / 2
        else:
            right = (right + left) / 2
    return right
