def get_gcd(num1: int, num2: int) -> int:
    if num2 > num1:
        num1, num2 = num2, num1

    while True:
        res = num1 % num2

        if res == 0:
            return num2

        num1, num2 = num2, res
