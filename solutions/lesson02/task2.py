def get_doubled_factorial(num: int) -> int:
    factorial = 1
    factorial_of_num = 1
    while 0 < num:
        factorial_of_num *= num
        num -= 2
    print(f"{factorial_of_num = }")
    return factorial
