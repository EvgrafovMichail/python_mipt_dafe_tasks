def count(n):
    ct = 0
    if n == 0:
        return 1
    while n > 0:
        n //= 10
        ct += 1
    return ct


def is_palindrome(num: int) -> bool:
    num_reversed = 0
    num_origin = num
    if num < 0:
        return False
    summ = count(num)
    t = summ // 2
    num_origin = num // (10 ** (t + summ % 2))
    while t > 0:
        num_reversed = num_reversed * 10 + (num % 10)
        t -= 1
        num //= 10
    return num_origin == num_reversed
