def get_amount_of_ways_to_climb(stair_amount: int) -> int:
    step_prev, step_curr = 1, 1
    # ваш код
    if stair_amount == 1:
        step_curr = 1
    elif stair_amount == 2:
        step_curr = 2
    else:
        step_prev, step_curr = 1, 2
        for _ in range(3, stair_amount + 1):
            step_prev, step_curr = step_curr, step_prev + step_curr
    return step_curr