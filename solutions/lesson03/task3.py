def get_nth_digit(num: int) -> int:
    digits = 1
    count = 5
    start = 0

    while True:
        block_len = count * digits
        if num <= block_len:
            break
        num -= block_len
        digits += 1
        start = 10 ** (digits - 1)
        end = 10**digits
        count = (end - start) >> 1

    index = (num - 1) // digits
    offset = (num - 1) % digits
    n = (start >> 1) + index
    even = n << 1
    power = digits - offset - 1

    return (even // (10**power)) % 10
