def get_amount_of_ways_to_climb(stair_amount: int) -> int:
    step_prev, step_curr, sum_of_prevs = 1, 2, 3
    if stair_amount < 4:
        return stair_amount
    else:
        for step in range(stair_amount - 2):
            sum_of_prevs = step_curr + step_prev
            step_prev = step_curr
            step_curr = sum_of_prevs
    return sum_of_prevs