def count(n):
    ct = 0
    if n == 0:
        return 1
    while n > 0:
        n //= 10
        ct += 1
    return ct


def is_palindrome(num: int) -> bool:
    t = count(num) // 2
    num2 = 0
    num1 = num // (10 ** (t))

    while t > 0:
        num2 += (num % 10) * 10 ** (t - 1)
        t -= 1
        num //= 10
    return num1 == num2
