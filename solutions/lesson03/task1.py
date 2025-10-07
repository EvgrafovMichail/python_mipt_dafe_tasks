def flip_bits_in_range(num: int, left_bit: int, right_bit: int) -> int:
    # ваш код
    if left_bit == 0:
        left_bit = 1
    cnt = right_bit - left_bit + 1
    mask = ((1 << cnt) - 1) << (left_bit - 1)
    return num ^ mask
