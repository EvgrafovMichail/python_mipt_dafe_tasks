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
         for i in range(2, stair_amount + 1):
             incremenator = step_prev
             step_prev = step_curr
             step_curr = step_curr + incremenator

    return step_curr
