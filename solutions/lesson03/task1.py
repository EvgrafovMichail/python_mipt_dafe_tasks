def flip_bits_in_range(num: int, left_bit: int, right_bit: int) -> int:
    power = 1
    position = 1
    result = 0
    while num > 0 or position <= right_bit:
        bit = num % 2
        num //= 2

        if left_bit <= position <= right_bit:
            bit = 1 - bit

        result += bit * power
        position += 1
        power *= 2

    return result
