def flip_bits_in_range(num: int, left_bit: int, right_bit: int) -> int:
    for i in range(left_bit, right_bit + 1):
        mask = 1 << (i - 1)
        num = num ^ mask
    return num
