def is_palindrome(num: int) -> bool:
    num_original = num
    num_reversed = 0
    while num > 0:
        num_reversed = num_reversed * 10 + num % 10
        num //= 10
    # ваш код
    return num_original == num_reversed
