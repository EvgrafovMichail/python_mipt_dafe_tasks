def get_gcd(num1: int, num2: int) -> int:
    nod = 0

    if num2 > num1:
        while num2 % num1 > 0:
            r = num2 % num1
            num2 = num1
            num1 = r
        nod = num1
    elif num1 > num2:
        while num1 % num2 > 0:
            r = num1 % num2
            num1 = num2
            num2 = r
        nod = num2
    else:
        nod = num1

    return nod


# print(get_gcd(int(input("num1 = ")), int(input("num2 = "))))
