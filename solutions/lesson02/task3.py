def get_amount_of_ways_to_climb(stair_amount: int) -> int:
    steps = [0] * (stair_amount + 1)
    steps[0] = 1
    steps[1] = 1

    for i in range(2, stair_amount + 1):
        steps[i] = steps[i - 1] + steps[i - 2]
    return steps[stair_amount]

