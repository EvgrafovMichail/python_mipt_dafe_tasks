def get_cube_root(n: float, eps: float) -> float:
    if n > 0:
        if n >= 1:
            left = 1
            right = n
        else:
            left = 0
            right = 1
        middle = (right + left) / 2
        while abs(middle**3 - n) > eps:
            if middle**3 == n:
                return middle
            elif middle**3 < n:
                left = middle
            elif middle**3 > n:
                right = middle
            middle = (right + left) / 2
    elif n < 0:
        if n <= -1:
            left = n
            right = -1
        else:
            left = -1
            right = 0
        middle = (right + left) / 2
        while abs(middle**3 - n) > eps:
            if middle**3 == n:
                return middle
            elif middle**3 < n:
                left = middle
            elif middle**3 > n:
                right = middle
            middle = (right + left) / 2
    elif n == 0:
        return 0
    return middle
