def get_amount_of_ways_to_climb(stair_amount: int) -> int:
    step_prev, step_curr, step_sum = 1, 2, 0
    if stair_amount < 4: 
        return stair_amount
    
    for step in range(stair_amount - 2):
        step_sum = step_curr + step_prev
        step_prev = step_curr
        step_curr = step_sum
    return step_sum

