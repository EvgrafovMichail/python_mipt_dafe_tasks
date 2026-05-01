def get_doubled_factorial(num: int) -> int:
    factorial = 1
    # ваш код
    if num <= 1:
        factorial = 1
    else:
        while num > 1:
            factorial *= num
            num -= 2
    return factorial
