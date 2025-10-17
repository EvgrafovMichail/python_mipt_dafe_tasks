def get_doubled_factorial(num: int) -> int:
    factorial = 1
    for i in range(1 + (num % 2 + 1) % 2, num + 1, 2):
        factorial *= i
    return factorial
