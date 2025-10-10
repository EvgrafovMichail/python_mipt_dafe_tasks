def get_doubled_factorial(num: int) -> int:
    
    factorial = 1
    if num == 0 or num == 1:
        return 1
    else:
        for i in range(num, 0, -2):
           factorial *= i

        return factorial

#print(get_doubled_factorial(int(input("num = "))))