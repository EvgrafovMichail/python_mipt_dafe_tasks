def get_amount_of_ways_to_climb(stair_amount: int) -> int:
    step_prev, step_curr = 1, 1
    if stair_amount == 1:
        return step_curr
    else:
        for i in range(2, stair_amount + 1):
            temp = step_curr
            step_curr = step_curr + step_prev
            step_prev = temp
            #Stair amount equals to element with index n+1 of fibonacci sequence
    return step_curr
