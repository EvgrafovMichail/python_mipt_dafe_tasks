def get_multiplications_amount(num: int) -> int:
    multiplications_amount = 0
    while num != 1:
        if num % 2 == 1:
            multiplications_amount += 1
            num -= 1
        else:
            multiplications_amount += 1
            num //= 2
    return multiplications_amount
print(get_multiplications_amount(133))