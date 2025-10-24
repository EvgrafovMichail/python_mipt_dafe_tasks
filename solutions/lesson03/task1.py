def flip_bits_in_range(num: int, left_bit: int, right_bit: int) -> int:
    MASK = 0
    for diapozon in range(left_bit - 1, right_bit):
        MASK = MASK | (1 << diapozon)

    num = int(num ^ MASK)
    return num


# print(flip_bits_in_range(
# int(input("num = ")),
# int(input("left_bit = ")),
# int(input("right_bit = "))))
