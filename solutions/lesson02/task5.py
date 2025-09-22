def get_gcd(num1: int, num2: int) -> int:
    ost = max(num1,num2)%min(num1,num2)
    
    if ost == 0:
        return min(num1,num2)
    else: 
        return(get_gcd(min(num1,num2),ost))