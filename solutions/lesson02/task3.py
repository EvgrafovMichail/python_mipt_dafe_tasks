from .task1 import get_factorial
def get_amount_of_ways_to_climb(stair_amount: int) -> int:
    step_prev, step_curr = 1, 1
    # ваш код
    counter=0
    if(stair_amount%2==0):

        for i in range(0,stair_amount+1,2):
           

            counter=counter+(get_factorial(i+(stair_amount-i)//2))//((get_factorial((stair_amount-i)//2))*get_factorial(i))
            

    else:
        for i in range(1,stair_amount+1,2):

            counter=counter+(get_factorial(i+(stair_amount-i)//2))//((get_factorial((stair_amount-i)//2))*get_factorial(i))

    return counter
