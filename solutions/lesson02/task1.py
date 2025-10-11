def get_factorial(num: int) -> int:
    factorial = 1

    for arg in range(1, num + 1):
        factorial *= arg

    return factorial


# print(get_factorial(int(input("num = "))))
