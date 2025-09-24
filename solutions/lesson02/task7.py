def is_palindrome(num: int) -> bool:
    
    s1=str(num)

    s2=''.join(reversed(s1))
    
    return s1 == s2
