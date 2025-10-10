def flip_bits_in_range(n: int, left: int, right: int) -> int:
    if n == 0: 
        return (2 ** (right - left + 1) - 1) << (left - 1)
    bn = 0
    pos = 1
    poscount = 1
    while n > 0:
        if (poscount <= right) and (poscount >= left):
            bn += (1 - (n & 1)) * pos
        else:
            bn += (n & 1) * pos
        pos *= 10
        n >>= 1
        poscount += 1
    des = 0
    pos = 0
    while bn:
        des ^= (bn % 10) << pos
        pos += 1
        bn //= 10
    return des