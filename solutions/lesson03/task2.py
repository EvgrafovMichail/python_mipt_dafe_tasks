
def mod(a: float):
    if a < 0:
        return -a
    else:
        return a


def get_cube_root(n: float, eps: float) -> float:
    left = 0
    sec = 0
    ans = 0
    min = 0
    if n < 0:
        n = -n
        min = 1
    right = n
    while 1:
        sec = (right + left) / 2
        if sec * sec * sec > n:
            right = sec
        else:
            left = sec
            right = sec * 2
        ans = right * right * right
        if mod(ans - n) < eps:
            if min == 1:
                right = -right
            return right