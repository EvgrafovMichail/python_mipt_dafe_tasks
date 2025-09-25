def get_gcd(a: int, b: int) -> int:
    while b != 0 and a != 0: 
        if a >= b: 
            a = a % b
        else: 
            b = b % a
    return a + b

    
