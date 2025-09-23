def get_gcd(num1: int, num2: int) -> int:
    # ваш код
    while num2:
        num1, num2 = num2, num1 % num2 
    return num1
