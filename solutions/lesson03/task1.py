def flip_bits_in_range(num: int, left_bit: int, right_bit: int) -> int:
    MASK = 0
    for i in range(left_bit, right_bit + 1):
        MASK = (1 << (i - 1)) | MASK
    return num ^ MASK
