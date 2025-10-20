def get_doubled_factorial(num: int) -> int:
    factorial = 1
    if num > 1 and num % 2 == 0:
        for i in range(2, num + 1, 2):
            factorial *= i
    elif num > 1 and num % 2 == 1:
        for i in range(1, num + 1, 2):
            factorial *= i
    else:
        factorial = 1
    return factorial
