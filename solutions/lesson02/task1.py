num = int(input())#Я вписал это до кода ибо иначе это не работает, я хз почему
def get_factorial(num: int) -> int:
    factorial = 1
    for i in range(1, num+1):
        factorial *=i
    return factorial
print(get_factorial(num))
