def is_palindrome(num: int) -> bool:
    num_reversed = 0
    num_origin = num
    # ваш код
    if num < 0:
        num_reversed = abs(num)
    else:
        num_origin = list(map(int, str(abs(num))))
        num_reversed = num_origin[::-1]
    return num_origin == num_reversed
