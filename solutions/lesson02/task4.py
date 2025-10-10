def get_multiplications_amount(num: int) -> int:
    #multiplications_amount = 0     - не нужен в данном варианте программы (используется в варианте с while)
    
    if num == 1:
        return 0
    
    if num % 2 == 0:
        return 1 + get_multiplications_amount(num // 2)
    
    if num % 2 == 1:
        return 1 + get_multiplications_amount(num - 1)
    
    #return multiplications_amount - не используем, 
    # т.к. не используется прерменная multiplications_amount

#print(get_multiplications_amount(int(input("num = "))))

"""Можно сделать вариант с while
def get_multiplications_amount(num: int) -> int:
    multiplications_amount = 0     
    
    while num > 1:
        if num % 2 == 0:
            num //= 2
        else:
            num -=1
        multiplications_amount +=1
    
    return multiplications_amount"""