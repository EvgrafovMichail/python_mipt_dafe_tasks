def flip_bits_in_range(num: int, left_bit: int, right_bit: int) -> int:
    bit = 0
    counter = 1
    result = 0

    while counter <= right_bit:
        bit = num & 1 if num != 0 else 0

        if right_bit >= counter >= left_bit:
            bit = 1 - bit

        print(result, bit)
        result = result + (bit << (counter - 1))
        print(result)
        num >>= 1
        counter += 1

    while num > 0:
        print(counter, result, bit)
        bit = num & 1
        result = result + (bit << (counter - 1))
        num >>= 1
        counter += 1

    return result
