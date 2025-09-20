def get_amount_of_ways_to_climb(stair_amount: int) -> int:
    step_prev, step_curr = 1, 1

    stairs = [1, 1, 2]
    for i in range(2, stair_amount):
        stairs.append(stairs[-1] + stairs[-2])
    step_curr = stairs[stair_amount]

    return step_curr
