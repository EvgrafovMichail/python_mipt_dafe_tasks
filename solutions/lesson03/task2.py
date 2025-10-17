def perebor(n: float, left: float, right: float, eps: float):
    mid = (left + right) / 2

    while abs(mid * mid * mid - n) > eps:
        if mid * mid * mid > n:
            right = mid

        else:
            left = mid

        mid = (left + right) / 2

    return mid


def get_cube_root(n: float, eps: float) -> float:
    if n > 1:
        left, right = 1, n
    elif n > 0:
        left, right = 0, 1
    else:
        left, right = n, 0
    n = perebor(n, left, right, eps)

    return n
