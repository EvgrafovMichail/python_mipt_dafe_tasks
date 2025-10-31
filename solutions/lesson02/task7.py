def is_palindrome(num: int) -> bool:
    num_reversed = 0
    num_origin = num
    n = 0
    while num >= 10**n:
        n += 1
    for i in range(1, n + 1):
        c = num_origin % 10
        k = n - i
        num_reversed += c * 10**k
        num_origin -= c
        num_origin /= 10
    num_origin = num
    return num_origin == num_reversed
