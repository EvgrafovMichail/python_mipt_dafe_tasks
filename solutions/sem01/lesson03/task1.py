def flip_bits_in_range(num: int, left_bit: int, right_bit: int) -> int:
    for i in range(left_bit - 1, right_bit):
        xor = 1 << i
        num = num ^ xor
    return num
