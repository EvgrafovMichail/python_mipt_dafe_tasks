def get_gcd(num1: int, num2: int) -> int:
    a = num1
    b = num2
    t = 0
    while a % b != 0:
        if a < b:
            t = a
            a = b
            b = t
        a = a % b
    num1 = b
    return num1
