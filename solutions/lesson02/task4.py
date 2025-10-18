def get_multiplications_amount(num: int) -> int:
    result = 0
    while num > 1:
        if num % 2 == 0:
            num //= 2
            result += 1
        else:
            num -= 1
            result += 1
    return result
