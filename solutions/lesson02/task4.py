def get_multiplications_amount(num: int) -> int:
    multiplications_amount = 0
    
    while num//2!=0:
        if num%2 == 1:
            multiplications_amount+=1
            num -= 1
        num = num//2
        multiplications_amount+=1
    return multiplications_amount