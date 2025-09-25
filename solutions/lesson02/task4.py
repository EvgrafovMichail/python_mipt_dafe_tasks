def get_multiplications_amount(num: int) -> int:
    multiplications_amount = 0
    while num>1:
        if num%2==0:
            multiplications_amount+=1
            num //= 2
        else:
            multiplications_amount+=1
            num-=1
    return multiplications_amount
