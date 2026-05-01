def chlen(n):
    if n == 0:
        return 1
    else:
        cnt = 0
        while n:
            n //= 10
            cnt += 1
        return cnt


def is_palindrome(num: int) -> bool:
    num_reversed = 0
    num_origin = num
    if num < 0:
        return 0
    a = chlen(num)
    while a > 0:
        num_reversed += (num % 10) * (10 ** (a - 1))
        num //= 10
        a -= 1
    return num_origin == num_reversed
