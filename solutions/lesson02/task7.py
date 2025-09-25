def is_palindrome(num: int) -> bool:
    num = str((num))
    for i in range(len(num) // 2 + 1):
        if num[i] != num[len(num) - i - 1]:
            return False
    return True
