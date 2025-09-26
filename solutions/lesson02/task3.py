def get_amount_of_ways_to_climb(stair_amount: int) -> int:
    step_prev, step_curr = 1, 1
    step_curr += 1
    if stair_amount <= 0:
        return 0
    if stair_amount == 1:
        return 1
    if stair_amount == 2:
        return 2
    else:
        for i in range(3, stair_amount + 1):
            steps = step_curr + step_prev
            step_prev = step_curr
            step_curr = steps

    return step_curr