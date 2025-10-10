def get_nth_digit(num: int) -> int:
    for r in range(1, 10):
        if num - (9 * 10 ** (r - 1) * 5 * (r + 1) + 5) > 0:
            s = 9 * 10**r - (num - (9 * 10 ** (r - 1) * 5 * (r + 1) + 5)) // (r + 1)
            c = 10**r + s // r + s % (r + 1)
            d = c // 10 ** (s % (r + 1))
            return d


print(get_nth_digit(10))
