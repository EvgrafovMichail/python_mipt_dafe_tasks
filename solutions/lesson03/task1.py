def flip_bits_in_range(num: int, left_bit: int, right_bit: int) -> int:
    mask1 = (1 << (right_bit - left_bit + 1)) - 1

    mask2 = (num >> (left_bit - 1)) & mask1

    num = num - (mask2 << (left_bit - 1))

    mask2 = mask2 ^ mask1

    num = num + (mask2 << (left_bit - 1))
    return num
