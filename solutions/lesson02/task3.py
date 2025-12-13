def get_amount_of_ways_to_climb(stair_amount: int) -> int:
    prev1, prev2 = 0, 1 
    for n in range(stair_amount + 1):
        current = prev1 + prev2
        prev1, prev2 = current, prev1
    return prev1