def get_multiplications_amount(num: int) -> int:
    multiplications_amount = 0
    while num > 1:
        
        if num % 2 == 0:
            multiplications_amount += 1
            num //= 2
        
        else:
            multiplications_amount += 1
            num -= 1
        
    return multiplications_amount


for i in range(1, 1001):
    print(i, get_multiplications_amount(i))
