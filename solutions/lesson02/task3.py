def get_amount_of_ways_to_climb(stair_amount: int) -> int:
    step_prev = 1
    step_curr = 1
    t = 0
    i = 1
    while i < stair_amount:
        t = step_curr
        step_curr = step_prev + t
        step_prev = t
        i += 1
    return step_curr
