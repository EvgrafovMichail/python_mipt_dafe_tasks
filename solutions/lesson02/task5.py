num1=int(input())
num2=int(input())
def get_gcd(num1: int, num2: int) -> int:
    if num1>num2:
        a=num1
        b=num2
    else:
        a=num2
        b=num1
    while a%b!=0:
        c=a%b #я полчаса тупил из-за того, что не записал остаток от деления в отдельную переменную, в таких циклах это важно как я понял
        a=b
        b=c
    num1 = b #в строке ниже лучше было-бы вместо num1 просто b написать, но я не совсем шарю критично ли это, надо спросить
    return num1 
