def get_doubled_factorial(num: int) -> int:
    factorial = 1

    if num % 2 == 0:
        for i in range(2, num + 1, 2):
            factorial *= i

    else:
        for i in range(1, num + 1, 2):
            factorial *= i

    return factorial
