def get_amount_of_ways_to_climb(stair_amount: int) -> int:
    step_prev, step_curr = 1, 1
    if stair_amount<=3:
        return stair_amount
    else:
        for i in range(stair_amount-1):
            t=step_prev
            step_prev=step_curr
            step_curr=step_curr+t
    return step_curr