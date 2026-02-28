def is_palindrome(num: int) -> bool:
    if num < 0:
        return False

    num_reversed = 0
    num_origin = num

    smax = 0
    for i in range(1, 10):
        if num // 10**i > 0:
            smax += 1

    s = smax
    while s != -1:
        n_s = num // 10**s
        num -= n_s * 10**s
        num_reversed += n_s * 10 ** (smax - s)
        s -= 1

    return num_origin == num_reversed
