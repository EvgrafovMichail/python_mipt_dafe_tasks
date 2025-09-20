def get_factorial(num: int) -> int:
    factorial_of_num = 1

    for i in range(1, num + 1):
        factorial_of_num *= i

    return factorial_of_num
