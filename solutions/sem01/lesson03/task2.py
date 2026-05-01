def get_cube_root(n: float, eps: float) -> float:
    # ваш код
    sign = -1.0 if n < 0 else 1.0
    a = abs(n)

    power = 0
    while (1 << power) ** 3 < a:
        power += 1
    left, right = 0.0, float(1 << power)

    while True:
        mid = (left + right) * 0.5
        err = mid * mid * mid - a
        if abs(err) <= eps:
            return sign * mid
        if err < 0:
            left = mid
        else:
            right = mid
