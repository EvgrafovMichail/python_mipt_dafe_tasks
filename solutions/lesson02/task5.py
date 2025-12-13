def get_gcd(num1: int, num2: int) -> int:
    num = max(num1, num2)
    num2 = min(num1, num2)
    num1 = num
    while num1 % num2 != 0:
        num = num1 % num2
        num1 = num2
        num2 = num
    num1 = num2
    return num1
