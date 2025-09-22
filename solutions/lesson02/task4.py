def get_multiplications_amount(num: int) -> int:
    multiplications_amount = 0
    x=bin(num)[3:]

    for i in x:
        if i=='1': multiplications_amount += 2
        else: multiplications_amount += 1
        
    return multiplications_amount