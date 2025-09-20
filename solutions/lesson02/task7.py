def is_palindrome(num: int) -> bool:
    if num < 0:
        return False
    num_reversed = int(str(num)[::-1])
    num_origin = num
    return num_origin == num_reversed
