def get_amount_of_ways_to_climb(stair_amount: int) -> int:
    if stair_amount <= 1:
        return 1
    step_prev, step_curr = 1, 1
    for i in range(2, stair_amount + 1):
        old_step_prev = step_prev
        old_step_curr = step_curr
        new_step_prev = old_step_curr
        new_step_curr = old_step_prev + old_step_curr
        step_prev = new_step_prev
        step_curr = new_step_curr
    return step_curr
