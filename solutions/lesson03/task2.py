from math import *

def get_cube_root(y: float, eps: float) -> float:

    l, r = -10 ** 8, 10 ** 8
    x = (l + r) / 2.0
    while abs(x ** 3 - y) * 10 > eps:
        x = (l + r) / 2.0
        if x ** 3 > y:
            r = x
        else:
            l = x

    return x



print(get_cube_root(int(input()), 0.0001))