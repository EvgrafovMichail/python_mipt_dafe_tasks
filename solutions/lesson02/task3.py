def get_amount_of_ways_to_climb(stair_amount: int) -> int:
    step_prev, step_curr = 1, 1
    for _ in range(1, stair_amount):
        step_prev, step_curr = step_curr, step_curr + step_prev
    return step_curr
