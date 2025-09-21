def is_palindrome(num: int) -> bool:
    num_reversed = 0
    num_origin = num
    s = str(num)
    num_origin = s  
    num_reversed = s[::-1]
    return num_origin == num_reversed
