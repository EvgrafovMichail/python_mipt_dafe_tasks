def is_palindrome(num: int) -> bool:
    num_reversed = 0
    num_origin = num
    # ваш код
    if num < 0:
        num_reversed = abs(num)
    else:
        num_origin = num
        num_reversed = 0
        while num > 0:
            digit = num % 10
            num_reversed = num_reversed * 10 + digit
            num //= 10
    return num_origin == num_reversed
