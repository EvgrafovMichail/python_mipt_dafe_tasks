def get_factorial(num: int) -> int:
    factorial = 1
    while 0 < num:
        factorial *= num
        num -= 1
    return factorial
