def get_gcd(num1: int, num2: int) -> int:
    if num1 == num2:
        return num1
    if num1 > num2:
        if num1 % num2 == 0:
            return num2
        else:
            return get_gcd(num2, num1 % num2)

    if num2 > num1:
        if num2 % num1 == 0:
            return num1
        else:
            return get_gcd(num1, num2 % num1)
