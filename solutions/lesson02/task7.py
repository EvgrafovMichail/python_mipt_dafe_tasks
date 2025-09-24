def is_palindrome(num: int) -> bool:
    num_origin = str(num)
    num_reversed = num_origin[::-1]

    return num_origin == num_reversed
