def is_palindrome(num: int) -> bool:
    if num < 0:
        return False
    num_reversed = str(abs(num))
    num_reversed = num_reversed[::-1]
    num_reversed = int(num_reversed)
    return num == num_reversed
