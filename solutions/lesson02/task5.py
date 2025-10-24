def get_gcd(num1: int, num2: int) -> int:
    while num1 != 0 and num2 != 0:
        if num1 >= num2:
            num1 %= num2
        else:
            num2 %= num1
    return num1 + num2
