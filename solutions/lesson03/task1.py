def flip_bits_in_range(num: int, left_bit: int, right_bit: int) -> int:
    return num ^ (((1 << (right_bit - left_bit + 1)) - 1) << (left_bit - 1))
