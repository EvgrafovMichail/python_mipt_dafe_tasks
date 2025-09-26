def get_gcd(num1: int, num2: int) -> int:
    while num1 > 0 and num2 > 0:
        if max(num1, num2) % min(num1, num2) == 0:
            gcd = min(num1, num2)
            break
        else:
            c = num1
            num1 = min(num1, num2)
            num2 = max(c, num2) % min(c, num2)
    return gcd
