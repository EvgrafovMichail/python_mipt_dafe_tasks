def flip_bits_in_range(num: int, left_bit: int, right_bit: int) -> int:
    for i in range(left_bit - 1, right_bit):
        bit = 1 << i
        num ^= bit
    return num
