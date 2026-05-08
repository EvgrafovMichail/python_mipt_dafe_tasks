def get_gcd(num1: int, num2: int) -> int:
    while max(num1, num2) % min(num1, num2) != 0:
        if num1 > num2:
            num1 = num1 % num2
        else:
            num2 = num2 % num1
    return min(num1, num2)
