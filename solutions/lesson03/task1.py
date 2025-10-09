def flip_bits_in_range(num: int, left_bit: int, right_bit: int) -> int:
    b = (1 << right_bit) - 1
    a = (1 << (left_bit-1)) -1
    one_ab = b ^ a
    num = num ^ one_ab
    return num

print(flip_bits_in_range(8,1,3))