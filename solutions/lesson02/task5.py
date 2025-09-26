def get_gcd(num1: int, num2: int) -> int:
    while True:
        if num2 > num1:
            if num2 % num1 == 0:
                return num1
            else:
                num2 = num2 % num1
        else:
            num2, num1 = num1, num2
    return num2
