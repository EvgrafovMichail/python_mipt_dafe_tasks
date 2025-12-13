def get_amount_of_ways_to_climb(stair_amount: int) -> int:
    step_prev, step_curr = 1, 1

    if stair_amount != 0 and stair_amount != 1:
        for _ in range(2, stair_amount + 1):
            step_prev, step_curr = step_curr, step_curr + step_prev

    return step_curr
