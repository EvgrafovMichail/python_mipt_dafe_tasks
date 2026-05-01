def is_palindrome(num: int) -> bool:
    num_reversed = 0
    num_origin = num

    num_origin = str(num_origin)
    num_reversed = num_origin[::-1]

    return num_origin == num_reversed
