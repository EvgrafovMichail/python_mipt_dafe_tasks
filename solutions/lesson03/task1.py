def flip_bits_in_range(num: int, left_bit: int, right_bit: int) -> int:
    position = left_bit

    while position <= right_bit:
        bit_weight = 2 ** (position - 1)
        bit_value = (num // bit_weight) % 2

        if bit_value == 0:
            num += bit_weight
        else:
            num -= bit_weight

        position += 1

    return num
