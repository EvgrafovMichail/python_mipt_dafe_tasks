def get_nth_digit(num: int) -> int:
    le = 1
    while True:
        first = 10 ** (le - 1) * int(le != 1)
        if num <= (b := (10**le - first) // 2 * le):
            m = (num - 1) % le
            number = first + 2 * ((num - 1) // le)
            while number >= 0:
                le -= 1
                if le == m:
                    return number % 10
                number //= 10
        le += 1
        num -= b
