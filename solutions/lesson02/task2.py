def get_doubled_factorial(num: int) -> int:
    factorial = 1
    if num % 2 == 0:
        for i in range(1, num // 2 + 1):
            factorial *= 2 * i
    else:
        for i in range(0, (num - num % 2) // 2 + 1):
            factorial *= 2 * i + 1
    return factorial
