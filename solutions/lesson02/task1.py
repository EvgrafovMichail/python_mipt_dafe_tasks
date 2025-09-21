def get_factorial(num: int) -> int:
    factorial = 1
    for i in range(num):
        factorial *= i
    return factorial

