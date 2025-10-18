def get_gcd(num1: int, num2: int) -> int:
    # ваш код
    if num1 < num2:
        num1, num2 = num2, num1
    
    # Алгоритм Евклида
    while num2 != 0:
        remainder = num1 % num2
        num1 = num2
        num2 = remainder
    return num1
