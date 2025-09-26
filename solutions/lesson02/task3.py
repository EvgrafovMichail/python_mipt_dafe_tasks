def get_amount_of_ways_to_climb(stair_amount: int) -> int:
    prev_step = 1
    before_prev_step = 1
    if stair_amount == 1:

        return 1
    else:
        for i in range(2, stair_amount + 1):
            step = prev_step + before_prev_step
            before_prev_step = prev_step
            prev_step = step
        return step
