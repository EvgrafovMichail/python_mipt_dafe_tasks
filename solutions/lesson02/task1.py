def get_factorial(num: int) -> int:
    factorial = 1
    factorial_of_num = 1
    while 0 < num:
        factorial_of_num *= num
        num -= 1
    print(f"{factorial_of_num = }")
    return factorial
