def get_amount_of_ways_to_climb(stair_amount: int) -> int:
    step_prev, step_curr = 0, 1

    for i in range(stair_amount):
        t = step_curr
        step_curr = step_curr + step_prev
        step_prev = t

    return step_curr
