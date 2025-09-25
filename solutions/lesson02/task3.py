def get_amount_of_ways_to_climb(stair_amount: int) -> int:
    step2 = 1
    step1 = 1
    N = 1
    if stair_amount > 1:
        for i in range(2, stair_amount + 1):
            N = step2 + step1
            step2, step1 = step1, N
    return N
