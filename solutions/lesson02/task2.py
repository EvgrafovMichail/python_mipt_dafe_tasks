def get_doubled_factorial(num: int) -> int:
    factorial = 1
    if num == 0:
        factorial = 1
    elif num % 2 == 0:
        for i in range(2,num+2,2):
            factorial *= i
    else:
        for i in range(1,num+2,2):
            factorial *= i
    return factorial
