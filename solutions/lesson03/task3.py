def get_nth_digit(num: int) -> int:
    if num <= 5:
        return (num - 1) * 2
    k = 2
    m = 95
    ost = num - 5
    while num > m:
        ost = num - m

        k += 1
        m += 45 * k * 10 ** (k - 2)

    n = 10 ** (k - 1) - 2 + 2 * ((ost + k - 1) // k)
    if ost % k == 0:
        return n % 10
    else:
        return (n // 10 ** (k - ost % k)) % 10
