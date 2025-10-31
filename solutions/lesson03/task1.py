def flip_bits_in_range(num: int, left_bit: int, right_bit: int) -> int:
    while left_bit <= right_bit:
        if (num // 2 ** (left_bit - 1) % 2) == 0:
            num += 2 ** (left_bit - 1)
        else:
            num -= 2 ** (left_bit - 1)
        left_bit += 1
    return num
