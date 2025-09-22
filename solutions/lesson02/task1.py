def get_factorial(num: int) -> int:
    factorial = 1
    for i in range(2,num+1):
        factorial*=i
    return factorial
