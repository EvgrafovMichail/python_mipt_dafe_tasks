def get_doubled_factorial(num: int) -> int:
    result = 1
    for i in range(num, 0, -2):
        result *= i
    return result
