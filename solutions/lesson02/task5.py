def get_gcd(num1: int, num2: int) -> int:
    while min(num1, num2) > 1:
        if num1 > num2:
            ost = num1 % num2
            if ost == 0:
                return num2
            else:
                num1 = ost
        else:
            ost = num2 % num1
            if ost == 0:
                return num1
            else:
                num2 = ost
    return 1
