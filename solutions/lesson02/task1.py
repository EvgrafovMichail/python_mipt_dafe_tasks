def get_factorial(num: int) -> int:
    factorial = 1
    for i in range(num, 0, -1):
        factorial *= i
    return factorial
