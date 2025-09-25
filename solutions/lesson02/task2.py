def get_doubled_factorial(num: int) -> int:
    factorial = 1
    if num > 1:
        for i in range(1 + int(num % 2 != 1), num + 1, 2):
            factorial *= i
        return factorial
    return 1
