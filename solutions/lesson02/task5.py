def get_gcd(num1: int, num2: int) -> int:
    if num1 == 0 or num2 == 0:
        num1 = max(num1, num2)
    elif num2 >= num1:
        while num2 % num1 != 0:
            num1 = num2 % num1
    elif num1 >= num2:
        while num1 % num2 != 0:
            num2 = num1 % num2
        num1 = num2
    return num1
