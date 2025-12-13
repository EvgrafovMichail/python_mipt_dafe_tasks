def get_doubled_factorial(num: int) -> int:
    factorial = 1
    for i in range(num, 0, -2):
        factorial *= i

    return factorial
