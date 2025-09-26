def get_gcd(num1: int, num2: int) -> int:
    if num1 < num2:
        num1, num2 = num2, num1
    d = num1 % num2
    while d != 0:
        num1, num2 = num2, d
        d = num1 % num2
    return num2
