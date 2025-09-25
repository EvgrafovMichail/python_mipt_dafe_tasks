def get_gcd(num1: int, num2: int) -> int:
    x, y = num1, num2

    while max(x, y) % min(x, y) != 0 and y != 0:
        temporary_val = x
        x = min(x, y)
        y = max(temporary_val, y) % min(temporary_val, y)

    gcd = min(x, y)
    return gcd
