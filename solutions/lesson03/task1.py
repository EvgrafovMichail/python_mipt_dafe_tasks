def flip_bits_in_range(num: int, left_bit: int, right_bit: int) -> int:
    mask1 = 1 << left_bit - 1
    mask2 = 1 << right_bit - 1
    extra_bit = 0
    if right_bit - left_bit - 1 == 0:
        maskprom = mask2
    elif right_bit - left_bit - 1 == 1:
        extra_bit = 1 << left_bit
        maskprom = extra_bit | mask2
    else:
        for i in range(left_bit, right_bit):
            extra_bit |= 1 << i
        maskprom = extra_bit | mask2

    maskfin = mask1 | maskprom
    num ^= maskfin
    
    return num
