def get_gcd(num1: int, num2: int) -> int:
    if num1 > num2:
        num1, num2 = num2, num1
    while num2 % num1 != 0:
        num2, num1 = num1, num2 % num1
    return num1
