def get_multiplications_amount(num: int) -> int:
    multiplications_amount = 0

    while num !=2 and num !=1 :
        if num %2== 0:
            num /=2
            multiplications_amount += 1
        else:
            num -=1
            multiplications_amount += 1
    multiplications_amount +=1
    if num == 1:
        multiplications_amount=0
    return multiplications_amount
