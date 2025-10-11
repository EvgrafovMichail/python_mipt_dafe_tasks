def flip_bits_in_range(num: int, left_bit: int, right_bit: int) -> int:
    if num == 0:
        return 2**right_bit - 1
    k = 0
    i = 1
    while num != 0:
        if left_bit <= i <= right_bit:
            k += ((num+1) % 2) * 10** (i-1)
            num //= 2
            i += 1
        else:
            k += (num%2)* 10**(i-1)
            num //= 2
            i += 1
    n = 0
    i = 0
    while k != 0:
        n += 2**(i) * (k % 10)
        i += 1
        k //= 10
    return n