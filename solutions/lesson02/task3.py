def get_amount_of_ways_to_climb(stair_amount: int) -> int:
    step_prev, step_curr = 1, 1
    if stair_amount == 1:
        return 1
    if stair_amount == 2:
        return 2
    for i in range(2, stair_amount + 1):
        step_prev, step_curr = step_curr, step_prev + step_curr
    return step_curr
