def is_palindrome(num: int) -> bool:
    if num < 0:
        return False
    if num < 10:
        return True

    num_reversed = 0
    original_num = num

    while num > 0:
        num_reversed = num_reversed * 10 + num % 10
        num //= 10

    return original_num == num_reversed
