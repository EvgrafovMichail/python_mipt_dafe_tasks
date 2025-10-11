def get_amount_of_ways_to_climb(stair_amount: int) -> int:
    step_prev, step_curr = 1, 2
    for i in range(1, stair_amount+1):
        if i % 2 == 1 and i > 2:
            step_prev += step_curr
        if i % 2 == 0 and i > 2:
            step_curr += step_prev
        if i == stair_amount:
            if i % 2 == 1:
                step_curr = step_prev
            break
    return step_curr