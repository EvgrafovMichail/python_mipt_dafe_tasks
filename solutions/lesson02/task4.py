def get_multiplications_amount(num: int) -> int:
    multiplications_amount=0
    i=num

    while(i>1):
        multiplications_amount+=1
        
        if (i%2==0):
            i/=2 
        
        else:
            i=i-1  
    
    return multiplications_amount
