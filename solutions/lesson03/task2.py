def get_cube_root(y: float, eps: float) -> float:
    left, right = -(10**8), 10**8
    x = (left + right) / 2.0
    while abs(x**3 - y) * 10 > eps:
        x = (left + right) / 2.0
        if x**3 > y:
            right = x
        else:
            left = x

    return x
