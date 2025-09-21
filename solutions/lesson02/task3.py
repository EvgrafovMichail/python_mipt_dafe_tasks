def get_amount_of_ways_to_climb(stair_amount: int) -> int:
    step_prev, step_curr = 1, 1
    # ваш код
    ways = [0]*(stair_amount+1)
    ways[0]=1
    ways[1]=1
    for i in range(2, stair_amount+1):
        ways[i] = ways[i-1] +ways[i-2]
    step_curr = ways[stair_amount]
    return step_curr
