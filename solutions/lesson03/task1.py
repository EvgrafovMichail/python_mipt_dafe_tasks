def flip_bits_in_range(num: int, left_bit: int, right_bit: int) -> int:
    length = right_bit - left_bit + 1

    ones_sequence = (1 << length) - 1

    mask = ones_sequence << (left_bit - 1)

    result = num ^ mask

    return result
