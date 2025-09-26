def get_doubled_factorial(n: int) -> int:
    factorial = 1
    for i in range(n, 0, -2):
        factorial *= i
    return factorial
