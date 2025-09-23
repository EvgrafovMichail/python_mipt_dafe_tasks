def get_gcd(num1: int, num2: int) -> int:
    balance = max(num1,num2) % min(num1,num2)
    if balance == 0: return min(num1,num2)
    
    while balance != 0:
        balance_old = balance
        balance = min(num1,num2) % balance_old
        if balance == 0: return balance_old