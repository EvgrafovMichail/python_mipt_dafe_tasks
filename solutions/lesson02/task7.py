def is_palindrome(num: int) -> bool:
    num_reversed = 0
    num_origin = num
    
    if num < 0:
        return False
    if num < 10:
        return True
    
    while num > 0:
        digit = num % 10
        num_reversed = num_reversed * 10 + digit
        num //= 10
    
    return num_origin == num_reversed