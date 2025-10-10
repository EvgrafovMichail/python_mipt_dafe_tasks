def get_cube_root(n: float, eps: float) -> float:
    count = 1
    minus = 0
    v = 0
    while n % 1 != 0:
        n *= 1000
        count *= 1000
    if n >= 0:
        minus = 1
    else:
        minus = -1
    n = int(abs(n))

    a = int(2*(1/eps))

    sk = n * a 

    for i in range(0, sk + 1):
        if i * i * i >= n * a * a * a:
            v = float(i)
            break
    g = 1
    while g * g * g != count:
        g *= 10
    return (minus * v) / a / g