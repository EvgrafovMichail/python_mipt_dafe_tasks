def get_amount_of_ways_to_climb(stair_amount: int) -> int:
    step_prev, step_curr = 0, 1
    for _ in range(stair_amount):
        step_curr, step_prev = step_curr + step_prev, step_curr
    return step_curr
