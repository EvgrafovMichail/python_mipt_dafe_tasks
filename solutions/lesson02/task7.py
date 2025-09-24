def is_palindrome(num: int) -> bool:
    if str(num) == str(num)[::-1]:
        return True
    else:
        return False
print(is_palindrome(13))
