def flip_bits_in_range(num: int, left_bit: int, right_bit: int) -> int:
    maska = ((1 << right_bit) - 1) ^ ((1 << (left_bit - 1)) - 1)

    return num^maska #Макаров Матвей 514

