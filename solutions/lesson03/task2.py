def get_cube_root(n: float, eps: float) -> float:
    g1, g2 = (n if n < 1 else 1), (1 if n < 1 else n)
    while True:
        num=(g1+g2)/2
        num_cube=num*num*num
        if (-eps<=num_cube-n<=eps): return num
        if (num_cube < n): g1=num
        else: g2=num
