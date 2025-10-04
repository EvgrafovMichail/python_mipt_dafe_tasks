def get_nth_digit(num: int) -> int:
    if num <= 5:
        return (num - 1) * 2
    num -= 6
    for i in range(1, 10):
        cnt = 5 * 10**i * (i + 1) - (i + 1) * 5 * 10 ** (i - 1)
        if num - cnt > 0:
            num -= cnt
        else:
            number_in = 10**i + num // (i + 1) * 2
            num %= i + 1
            return int(str(number_in)[num])
