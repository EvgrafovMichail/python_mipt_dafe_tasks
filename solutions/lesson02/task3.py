def get_amount_of_ways_to_climb(stair_amount: int) -> int:
    prev1, prev2 = 0, 1 
    for n in range(stair_amount + 1):
        current = prev1 + prev2
        prev1, prev2 = current, prev1
    return prev1
<<<<<<< HEAD

=======
>>>>>>> 570d5112c7b91279809cacc78e469fc98a5febbd
