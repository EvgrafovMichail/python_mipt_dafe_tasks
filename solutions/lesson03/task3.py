def get_nth_digit(num: int) -> int:
    n = 2 * (num - 1)
    while n > 10:
        n //= 10
    return n
