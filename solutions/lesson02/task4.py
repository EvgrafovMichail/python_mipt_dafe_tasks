def get_multiplications_amount(num: int, multiplications_amount = 0) -> int:
    if num == 1: 
        return multiplications_amount
    else: 
        if num % 2 == 0: 
            return get_multiplications_amount(num // 2, multiplications_amount + 1)
        else:
            return get_multiplications_amount(num - 1, multiplications_amount + 1)
        
print(get_multiplications_amount(10))

