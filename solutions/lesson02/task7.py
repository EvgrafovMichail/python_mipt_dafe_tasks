def is_palindrome(num: int) -> bool:
    num_reversed = 0
    num_origin = num
    if num == 0:
        return True
    if num % 10 == 0:
        return False
    if num < 0:
        return False
    while num_origin != 0:
        num_reversed = (num_origin % 10) + num_reversed * 10
        num_origin //= 10
    return num == num_reversed
