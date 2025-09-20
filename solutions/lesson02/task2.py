def get_doubled_factorial(num: int) -> int:
    factorial = 1
    if num <= 1:
        factorial *= 1
    else:
        factorial*=num*get_doubled_factorial(num-2)
    return factorial
