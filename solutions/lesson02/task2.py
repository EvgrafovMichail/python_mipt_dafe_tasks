num = int(input())#опять же хз, но если это поставить похзже, то оно не работает
#в целом тут просто n(n-2)(n-4) и т.д. поэтому ограничить надо ток 1 и 0, а остальное с условием моим вроде норм работает
def get_doubled_factorial(num: int) -> int:
    factorial = 1 
    if num <= 1:
        return 1 
    else: 
        while 0<=num-2:
            factorial *= num
            num = num - 2
    return factorial 
print(get_doubled_factorial(num))