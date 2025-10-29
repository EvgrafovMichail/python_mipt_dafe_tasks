def flip_bits_in_range(num: int, left_bit: int, right_bit: int) -> int:
    a = ((0b1 << (right_bit - left_bit + 1)) - 0b1) << (left_bit - 0b1)

    num = num ^ a

    return num
