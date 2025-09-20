def get_doubled_factorial(num: int) -> int:
    factorial = 1
    if num>1:
        return num*get_doubled_factorial(num-2)
    if num<=1:
        return 1
    return factorial