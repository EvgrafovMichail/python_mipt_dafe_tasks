def get_gcd(num1: int, num2: int) -> int:
    if num1 > num2: 
        mx = num1
        mn = num2
    else: 
        mx = num2
        mn = num1
    balance = mx % mn

    if balance == 0: 
        return mn
    
    while balance != 0:
        balance_old = balance
        balance = mn % balance_old
        if balance == 0: 
            return balance_old