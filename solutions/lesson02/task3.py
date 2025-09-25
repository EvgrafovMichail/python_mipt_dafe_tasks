def get_amount_of_ways_to_climb(stair_amount: int) -> int:
    step_prev, step_curr = 1, 1
    if stair_amount <= 1:
        return 1

    return 2 ** (stair_amount - 1)
