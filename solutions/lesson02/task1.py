def get_factorial(num: int) -> int:
    factorial = 1
    for x in range(2, num):
        factorial *= x
    return factorial
