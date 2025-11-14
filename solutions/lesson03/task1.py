def flip_bits_in_range(num: int, left_bit: int, right_bit: int) -> int:
    mask = (1 << (right_bit - left_bit + 1)) - 1
    mask <<= left_bit - 1
    return num ^ mask


print(bin(flip_bits_in_range(1, 5, 10)))
