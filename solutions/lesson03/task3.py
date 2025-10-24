def get_nth_digit(n: int) -> int:
    length = 1
    count = 0
    while True:
        digits_in_block = count * length
        if n > digits_in_block:
            n -= digits_in_block
            length += 1
            start = 10 ** (length - 1)
            count = (9 * 10 ** (length - 1)) // 2
        else:
            break
    index = (n - 1) // length
    num = start + (index * 2)
    pos_from_left = (n - 1) % length
    divisor = 10 ** (length - pos_from_left - 1)
    digit = (num // divisor) % 10

    return digit
