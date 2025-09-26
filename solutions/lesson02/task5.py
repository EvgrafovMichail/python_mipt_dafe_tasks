def get_gcd(num1: int, num2: int) -> int:
    while num2 != 0:
        temp = num2
        num2 = num1%num2
        num1=temp
    return num1
    