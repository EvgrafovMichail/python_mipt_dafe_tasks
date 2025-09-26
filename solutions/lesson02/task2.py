def get_doubled_factorial(num: int) -> int:
    factorial = 1
    while(0<num):
        factorial *=num
        num-=2
    return factorial
