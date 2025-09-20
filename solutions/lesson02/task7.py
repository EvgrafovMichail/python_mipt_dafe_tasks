def is_palindrome(num: int) -> bool:
    num_reversed = str(num)[::-1]
    num_origin = str(num)
    return num_origin == num_reversed
