def get_amount_of_ways_to_climb(stair_amount: int) -> int:
    n = stair_amount
    ways = 0
    if stair_amount <= 0:
        pass
    elif stair_amount == 1:
        ways += 1
    elif stair_amount == 2:
        ways += 2
    else:
        ways = ways + get_amount_of_ways_to_climb(n-1) + get_amount_of_ways_to_climb(n-2)
    return ways