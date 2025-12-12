def get_doubled_factorial(num: int) -> int:
    factorial = 1
    for i in range(num, 0, -2):
        if i == 0 or i == 1:
            break
        factorial *= i
    return factorial
