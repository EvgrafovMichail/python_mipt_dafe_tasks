def is_palindrome(num: int) -> bool:
    num_reversed = 0
    num_origin = num
    if str(num)==str(num)[::-1]:
        return True
    return False
    return num_origin == num_reversed
