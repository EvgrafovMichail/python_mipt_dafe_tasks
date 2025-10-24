def flip_bits_in_range(num: int, left_bit: int, right_bit: int) -> int:
    # ваш код
    count_bits = right_bit - left_bit + 1
    mask = (1 << count_bits) - 1
    mask <<= (left_bit - 1)
    return num ^ mask