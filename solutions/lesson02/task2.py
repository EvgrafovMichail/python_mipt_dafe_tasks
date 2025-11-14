def get_doubled_factorial(num: int) -> int:
    factorial = 1
    i = 0
    if num % 2 == 1:
        i = 1
        while i <= num:
            factorial = factorial * i
            i += 2
        return factorial

    if num % 2 == 0:
        i = 2
        while i <= num:
            factorial = factorial * i
            i += 2
        return factorial
