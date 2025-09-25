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
        c=a%b
        a=b
        b=c
    num1 = b
    return num1 
