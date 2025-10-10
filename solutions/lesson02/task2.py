def get_doubled_factorial(num: int) -> int:
    a, b = 2, 1  # вычислим 2!!, 1!! и 0!!
    if num == 0 or num == 1: return 1
    for n in range(3, num + 1):
        a, b = n * b, a
    return a
