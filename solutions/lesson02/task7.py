def is_palindrome(num: int) -> bool:
    num_reversed = 0
    num_origin = num
    while num > 0:
        num_reversed *= 10
        num_reversed += num % 10
        num //= 10
    return num_origin == num_reversed
