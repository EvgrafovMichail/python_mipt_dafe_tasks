def flip_bits_in_range(num: int, left_bit: int, right_bit: int) -> int:
    range = (1 << right_bit - left_bit + 1) - 1
    mask = range << left_bit - 1
    num ^= mask
    return num
