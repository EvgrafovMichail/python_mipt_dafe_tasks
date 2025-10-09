def flip_bits_in_range(num: int, left_bit: int, right_bit: int) -> int:
    new_num = 0
    p = 1
    while num > 0:
        new_num += num % 2 * p
        p *= 10
        num //= 2
    num = new_num
    for i in range(right_bit - 1, left_bit - 2, -1):
        if num // 10 ** i % 10 == 1:
            num -= 10 ** i
        else:
            num += 10 ** i
    new_num = 0
    p = 0
    while num > 0:
        new_num += num % 10 * 2 ** p
        p += 1
        num //= 10
    return new_num
