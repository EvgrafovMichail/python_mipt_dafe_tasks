def get_nth_digit(num: int) -> int:
    i = 1
    digit = 0
    while i < num:
        digit += 2
        if digit < 10:
            i += 1
        else:
            lenght = 0
            copy = digit
            while copy > 0:
                lenght += 1
                copy //= 10
            for j in range(lenght - 1, -1, -1):
                if i + (lenght - j) == num:
                    return digit // 10 ** (j) % 10
            i += lenght
    return digit