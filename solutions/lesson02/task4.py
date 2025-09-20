def get_multiplications_amount(num: int) -> int:
    multiplications_amount = 0
    if num==1:
        return 1
    if num==2:
        return 1
    if num%2==0:
        multiplications_amount+=1
        multiplications_amount+=get_multiplications_amount(num//2)
    else:
        multiplications_amount+=1
        multiplications_amount+=get_multiplications_amount(num-1)
    return multiplications_amount