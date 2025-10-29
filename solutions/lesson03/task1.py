def flip_bits_in_range(num: int, left_bit: int, right_bit: int) -> int:
<<<<<<<<< Temporary merge branch 1
    mask = 0
    for i in range(left_bit, right_bit + 1):
        mask += 2 ** (i - 1)

    return num ^ mask
=========
    # ваш код
    return num
>>>>>>>>> Temporary merge branch 2
