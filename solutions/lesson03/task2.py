def get_cube_root(n: float, eps: float) -> float:
    if n == 0:
        return 0
    sign = 1 if n >= 0 else -1
    result = 0
    a = 0
    abs_n = abs(n)
    b = abs_n if abs_n >= 1 else 1 / abs_n
    while abs(result * result * result - abs_n) > eps / 10:
        result = (a + b) / 2
        if result * result * result >= abs_n:
            b = result
        else:
            a = result
    return sign * result
