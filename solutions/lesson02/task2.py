def get_doubled_factorial(num: int) -> int:
    a, b, c = 2, 1, 1 #вычислим 2!!, 1!! и 0!! 
    for n in range(3, num+1):
        a, b, c = n*b, a, b
    return a
