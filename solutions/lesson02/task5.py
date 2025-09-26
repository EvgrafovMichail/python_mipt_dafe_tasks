def get_gcd(num1: int, num2: int) -> int:
    m = max(num1, num2)
    n = min(num1, num2)
    while n != 0:
        k = n
        n = m % n
        m = k
    return m
