def get_doubled_factorial(num: int) -> int:
    factorial = 1
    while num > 0:
        factorial *= num
        num -= 2
    return factorial
