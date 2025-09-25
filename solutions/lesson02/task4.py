def get_multiplications_amount(deg: int) -> int:
    multiplications_amount = 0
    while deg > 1:
        if deg % 2 == 0:
            multiplications_amount += 1
            deg = deg // 2
        else:
            multiplications_amount += 1
            deg -= 1
    return multiplications_amount
