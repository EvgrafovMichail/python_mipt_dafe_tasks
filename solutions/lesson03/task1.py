def flip_bits_in_range(num: int, left_bit: int, right_bit: int) -> int:
    # ваш код

    if left_bit > right_bit:
        a = left_bit
        left_bit = right_bit
        right_bit = a

    MASK = ((1 << (right_bit - left_bit + 1)) - 1) << (left_bit - 1)
    num = num ^ MASK

    return num
