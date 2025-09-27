def get_amount_of_ways_to_climb(stair_amount: int) -> int:
    step_prev, step_curr = 1, 1
    step_prev2 = 0

    if stair_amount >= 1:
        for _ in range (1, stair_amount +1):
         step_curr = step_prev + step_prev2
         step_prev, step_prev2 = step_curr, step_prev # Одновременная замена переменных 
        return(step_curr)
    else: 
        return("Error")
