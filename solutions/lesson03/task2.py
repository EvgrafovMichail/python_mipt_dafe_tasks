def get_cube_root(n: float, eps: float) -> float:
    if abs(n) < 1:
        left = 0
        right = abs(n + 1)
        middle = (left + right) / 2
    elif abs(n) > 1:
        left = 1
        right = abs(n)
        middle = (left + right) / 2
    else:
        return n

    while abs(middle**3 - abs(n)) >= eps:
        if middle**3 - abs(n) >= eps:
            right = middle
        else:
            left = middle
        middle = (right + left) / 2

    if n != 0:
        return middle * (n / abs(n))
    else:
        return 0