def get_gcd(num1: int, num2: int) -> int:
    d = max(num1, num2) % min(num1, num2)
    while d != 0:
        num1, num2 = min(num1, num2), d
        d = num1 % d
    return min(num1, num2)
