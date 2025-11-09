def get_factorial(num: int) -> int:
    factorial_of_num = 1

    for i in range(1, num + 1):
        factorial_of_num *= i

    return factorial_of_num


def get_amount_of_ways_to_climb(stair_amount: int) -> int:
    counter = 0

    if stair_amount % 2 == 0:
        for i in range(0, stair_amount + 1, 2):
            counter = counter + (
                get_factorial(i + (stair_amount - i) // 2)
                // (get_factorial((stair_amount - i) // 2) * get_factorial(i))
            )
    else:
        for i in range(1, stair_amount + 1, 2):
            counter = counter + (
                get_factorial(i + (stair_amount - i) // 2)
                // (get_factorial((stair_amount - i) // 2) * get_factorial(i))
            )

    return counter
