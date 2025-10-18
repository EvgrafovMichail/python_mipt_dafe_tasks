def get_nth_digit(num: int) -> int:
    for r in range(10, 0, -1):
        t = num - ((9 * 10 ** (r - 1) / 2) * r + 5)
        if t > 0:
            s = 10**r / 2 + t // (r + 1)
            n = t % (r + 1)
            c = 2 * s - 1
            d = (c + 1) % 10**n
            return d


print(get_nth_digit(1000))
