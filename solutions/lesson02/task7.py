def is_palindrome(num: int) -> bool:
    return str(num) == str(num)[::-1]