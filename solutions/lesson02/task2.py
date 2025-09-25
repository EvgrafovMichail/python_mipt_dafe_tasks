def get_doubled_factorial(num: int) -> int:
    factorial = 1
    if num <= 1:
        return 1
    else:
        while 0 <= num - 2:
            factorial *= num
            num = num - 2
    return factorial