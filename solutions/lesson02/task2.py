def get_doubled_factorial(num: int) -> int:
    factorial = 1
    while num > 1:
        factorial*=num
        num-=2
    return factorial
