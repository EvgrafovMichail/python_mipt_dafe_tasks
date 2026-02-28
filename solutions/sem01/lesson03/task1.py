def flip_bits_in_range(num: int, left_bit: int, right_bit: int) -> int:
    n = num
    s = 0
    while n:
        s += 1
        n //= 2

    t = s
    new_num = 0

    for i in range(left_bit - 1):
        r = 0 if num % 2 == 0 else 1
        new_num += r * 2 ** (s - t)
        num //= 2
        t -= 1

    for j in range(right_bit - left_bit + 1):
        r = 1 if num % 2 == 0 else 0
        new_num += r * 2 ** (s - t)
        num //= 2
        t -= 1

    for k in range(t):
        r = 0 if num % 2 == 0 else 1
        new_num += r * 2 ** (s - t)
        num //= 2
        t -= 1

    return new_num
