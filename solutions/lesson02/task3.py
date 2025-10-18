def get_amount_of_ways_to_climb(stair_amount: int) -> int:
    previous = 1
    current = 2
    result = 3
    if stair_amount < 4:
        return stair_amount

    for step in range(stair_amount - 2):
        result = current + previous
        previous = current
        current = result
    return result
