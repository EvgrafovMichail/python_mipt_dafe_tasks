def get_gcd(num1: int, num2: int) -> int:
    if num1 > num2:
        newMin = num2 
        while num1 % newMin != 0 and newMin != 0:
            newMin = num1 % newMin
            num1=num2
        num1=newMin
    else:
        newMin = num1 
        while num2 % newMin !=0 and newMin != 0 :
            newMin = num2% newMin
            num2=num1
        num1=newMin        
    return num1
