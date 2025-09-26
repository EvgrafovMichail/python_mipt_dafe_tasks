def get_amount_of_ways_to_climb(stair_amount: int) -> int:
    ways = (((1+5**0.5)/2)**(stair_amount+1)-((1-5**0.5)/2)**(stair_amount+1))/(5**0.5)
    iways=int(ways)
    return iways



