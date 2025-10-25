def is_palindrome(num: int) -> bool:
    if num < 0:
        return False
    num_reversed = 0
    num_reversed += num % 10
    num_current = num
    num_current //= 10
    while num_current > 0:
        num_reversed *= 10
        num_reversed += num_current % 10
        num_current //= 10
    return num == num_reversed
