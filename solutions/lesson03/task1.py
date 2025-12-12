def flip_bits_in_range(num: int, left_bit: int, right_bit: int) -> int:
    mask1 = 1 << left_bit - 1

    for i in range(left_bit + 1, right_bit + 1):
        mask1 |= 1 << i - 1  # 1 где надо поменять, остальное 0

    return num ^ mask1
