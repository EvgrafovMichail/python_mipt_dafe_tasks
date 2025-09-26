def is_palindrome(num: int) -> bool:
    palindrome = 0
    numm = num

    if num < 0:
        return False

    while num != 0:
        palindrome = palindrome * 10 + num % 10
        num //= 10

    if numm == palindrome:
        return True
    else:
        return False
