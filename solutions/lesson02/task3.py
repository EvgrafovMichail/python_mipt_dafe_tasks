def get_amount_of_ways_to_climb(stair_amount: int) -> int:
    step_prev, step_curr = 1, 1
    for i in range(1, stair_amount):
        var = step_prev + step_curr
        step_prev = step_curr
        step_curr = var

    return step_curr


# print(get_amount_of_ways_to_climb(int(input("stair_amount = "))))
