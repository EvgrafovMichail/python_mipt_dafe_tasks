def is_palindrome(num: int) -> bool:
    if num < 0:
        return False
    if num < 10:
        return True
    reversed_num = 0
    num_copy = num
    while num > 0:
        digit = num % 10
        reversed_num = reversed_num * 10 + digit
        num = num // 10
    return num_copy == reversed_num
