def get_nth_digit(num: int) -> int:
    len = 1
    count = 5
    start = 0

    while num > len * count:
        num -= len * count
        len += 1
        if len == 2:
            count = 45
            start = 10
        else:
            count *= 10
            start *= 10

    num_ind = (num - 1) // len
    dig_ind = (num - 1) % len
    numb = start + num_ind * 2

    pos = len - 1 - dig_ind
    digit = (numb // (10**pos)) % 10
    return digit
