def get_gcd(num1: int, num2: int) -> int:
    mi, ma = sorted([num1, num2])
    while True:
        ost = ma % mi
        if ost == 0:
            return mi
        mi, ma = sorted([mi, ost])
