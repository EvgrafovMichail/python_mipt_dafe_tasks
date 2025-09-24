def get_doubled_factorial(num: int) -> int:
    factorial = 1
    if num > 1 and num%2 == 0:
#Так как для функции двойного факторила важно число четно или нечетно, я сделал два пути для подсчета двойного факториала числа 
#(если оно > 1), поэтому начинаю цикл for или с 1 или с 2, с шагом 2
        for i in range(2, num + 1, 2):
            factorial *= i
    elif num > 1 and num%2 == 1:
        for i in range(1, num + 1, 2):
            factorial *= i
    else:
        factorial = 1 
    return factorial
