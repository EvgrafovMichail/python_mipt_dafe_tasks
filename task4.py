def get_multiplications_amount(num: int) -> int:
    multiplications_amount = 0

    if num == 1:
       return(1)
    
    while num > 1:
        if num % 2 == 0:
            num /= 2
        else:
            num -= 1
        multiplications_amount += 1  
    return multiplications_amount 

    
