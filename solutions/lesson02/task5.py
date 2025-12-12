def get_gcd(num1: int, num2: int) -> int:
    num1, num2 = min(num1, num2), max(num1, num2)
    while num2 % num1 != 0:
        num1, num2 = num2 % num1, num1
    return num1
