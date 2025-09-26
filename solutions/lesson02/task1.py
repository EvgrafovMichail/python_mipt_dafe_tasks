def get_factorial(num: int) -> int:
    factorial = 1
    for x in range(2, num + 1):
        factorial *= x
    return factorial
