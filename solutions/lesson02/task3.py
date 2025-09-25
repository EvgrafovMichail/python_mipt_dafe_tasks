def get_amount_of_ways_to_climb(stair_amount: int) -> int:
    for i in range(1, stair_amount):
        steps = step_curr + step_prev
        step_curr = step_prev
        step_prev = steps
    return step_curr
