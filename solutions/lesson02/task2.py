def get_doubled_factorial(num: int) -> int:
    
    factorial_of_num = 1

    if(num%2==0):
        start=2
    else:
        start=1
        
    for i in range(start, num + 1, 2):
        factorial_of_num *= i
    
    return factorial_of_num

