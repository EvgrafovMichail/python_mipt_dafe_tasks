def get_nth_digit(num: int) -> int:
    if num <= 5:
        return 2 * (num - 1)

    q = 5
    r = 1
    w = 0
    while q < num:
        w = q
        q += 45 * 10 ** (r - 1) * (r + 1)
        r += 1
    d = num - w
    count = (d + r - 1) // r
    res = 10 ** (r - 1) + 2 * (count - 1)
    last_num = count * r
    while last_num - d:
        res //= 10
        last_num -= 1

    return res % 10
