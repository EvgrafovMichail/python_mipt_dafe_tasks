def get_amount_of_ways_to_climb(stair_amount: int) -> int:
    step_prev, step_curr = 1, 1
    for i in range(stair_amount-1):
        temp = step_curr
        step_curr += step_prev
        step_prev = temp
    return step_curr