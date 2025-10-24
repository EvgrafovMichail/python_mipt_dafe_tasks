def get_nth_digit(num: int) -> int:
    i = 0

    while num > 5 * 10**i * (i + 1) - 5 * 10 ** (i - 1) * i:
        i += 1
        num -= 5 * 10**i * (i + 1) - 5 * 10 ** (i - 1) * i

    k = 5 * 10 ** (i - 1) + num // i + 1
    N = 2 * k
    return (N // 10 ** (i - 1 - (num - 1) % i)) % 10
