def get_gcd(num1: int, num2: int) -> int:
    # ваш код

    if num2 > num1:

        while (num2 % num1 != 0):
            remainder = num2 % num1
            num2 = num1
            num1 = remainder

    elif num1 > num2:

        while (num1 % num2 != 0):
            remainder = num1 % num2
            num1 = num2
            num2 = remainder
        num1 = num2    

    return num1