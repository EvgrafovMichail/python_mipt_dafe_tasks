def get_doubled_factorial(num: int) -> int:
    factorial = 1
    for i in range(num, 1, -2):
        if i > 1:
            factorial *= i
    return factorial
