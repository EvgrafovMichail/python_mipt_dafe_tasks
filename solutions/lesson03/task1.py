def flip_bits_in_range(num: int, left_bit: int, right_bit: int) -> int:
    mask = 0
    for i in range(left_bit - 1, right_bit):
        mask += 1 << i
    return num ^ mask
