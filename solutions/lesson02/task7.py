def is_palindrome(num: int) -> bool:
    num_reversed = 0
    
    num_origin = num
    
    if num<0:
        return False
    
    length=1
    
    while num//(10**length)!=0:
        length+=1
    
    for i in range(1,length+1):
        num_reversed+=(num%10)*10**(length-i)
        num//=10

    return num_origin == num_reversed
