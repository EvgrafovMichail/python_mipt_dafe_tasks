def is_palindrome(num: int) -> bool:
    num_origin = num
    num_reversed = str(abs(num))[::-1]
    print(num_origin, num_reversed)
    return abs(num_origin) == int(num_reversed)