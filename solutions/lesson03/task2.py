def get_cube_root(n: float, eps: float) -> float:
    if n == 0:
        return 0.0
    sign = 1 if n > 0 else -1  # знак искомого числа
    n = abs(n)
    if n > 1:  # границы бинпоиска
        left = 0
        right = n
    else:
        left = n
        right = 1
    binP = (left + right) / 2
    while abs(binP * binP * binP - n) > eps:  # сам алгос бинпоиска
        binP = (left + right) / 2
        cubeBin = binP * binP * binP
        if cubeBin > n:
            right = binP
        else:
            left = binP
    return sign * binP
