def get_factorial(num: int) -> int:
    factorial = 1
    i = 2
    while i <= num:
        factorial = factorial * i
        i += 1

    return factorial
