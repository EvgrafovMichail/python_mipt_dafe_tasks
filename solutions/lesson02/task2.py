def get_doubled_factorial(n: int) -> int:
    return 1 if n <= 1 else n * get_doubled_factorial(n - 2)
    
    


