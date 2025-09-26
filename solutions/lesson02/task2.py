def get_doubled_factorial(num: int) -> int:
    factorial = 1
    if num <= 1: 
        return 1
    for i in range(num, 1, -2):
        factorial *= i  
    return factorial
