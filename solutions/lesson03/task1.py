def flip_bits_in_range(num: int, left_bit: int, right_bit: int) -> int:
    num = num^((~(1 << right_bit) - ~(1 << left_bit - 1))*(-1))
    return num