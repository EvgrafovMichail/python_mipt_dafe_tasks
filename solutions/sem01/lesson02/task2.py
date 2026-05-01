def get_doubled_factorial(num: int) -> int:
    factorial = 1
    f0 = 1  # значение (n-2)!!
    f1 = 1  # значение (n-1)!!
    if num > 1:
        for i in range(2, num + 1):
            factorial = i * f0
            f0, f1 = f1, factorial

    return factorial
