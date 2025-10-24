def is_palindrome(num: int) -> bool:
    num_reversed = 0
    num_origin = num
    if str(num) == str(num)[::-1]:
        num_reversed = num
    return num_origin == num_reversed
