def flip_bits_in_range(num: int, left_bit: int, right_bit: int) -> int:
    A = 0
    for i in range(left_bit - 1, right_bit):
        edinichki = 1 << i
        A = A | edinichki
    num = num ^ A
    return num
