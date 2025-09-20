def get_gcd(a: int, b: int) -> int:
    if a == 0: 
        return b
    return get_gcd(b % a, a)
    
