def get_amount_of_ways_to_climb(stair_amount: int) -> int:
    step_prev, step_curr = 1, 1
    # ваш код
    if stair_amount == 0:
        step_curr = 0
    
    elif stair_amount == 1:
        step_curr = 1

    elif stair_amount == 2:
        step_curr = 2
    
    else:
        step_prev = [0]*(stair_amount + 1)
        
        step_prev[1] = 1

        step_prev[2] = 2

        for i in range (3, stair_amount + 1):
            step_prev[i] = step_prev[i - 1] + step_prev[i - 2]

        step_curr = step_prev[stair_amount]   

    return step_curr
