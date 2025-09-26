def is_palindrome(num: int) -> bool:
    pal = 0
    old_num = num
    if num < 0: 
        return False
    if 0 <= num < 10: 
        return True
    while num > 0:
        pal = pal * 10 + num % 10 
        num //= 10
    return pal == old_num