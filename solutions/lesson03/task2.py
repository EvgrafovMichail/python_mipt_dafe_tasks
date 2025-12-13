def get_cube_root(n: float, eps: float) -> float:
    if n == 1 or n == -1 or n == 0:
        return n
    elif 0 < n < 1:
        a = 1
        b = n
        x = n / 2
        while abs(x**3 - n) >= eps:
            if abs(x**3) < abs(n):
                b = x
            elif abs(x**3) > abs(n):
                a = x
            x = (a + b) / 2
    elif -1 < n < 0:
        a = -1
        b = n
        x = n / 2
        while abs(x**3 - n) >= eps:
            if abs(x**3) < abs(n):
                b = x
            elif abs(x**3) > abs(n):
                a = x
            x = (a + b) / 2
    else:
        a = n
        b = 0
        x = n / 2
        while abs(x**3 - n) >= eps:
            if abs(x**3) > abs(n):
                a = x
            elif abs(x**3) < abs(n):
                b = x
            x = (a + b) / 2
    return x
