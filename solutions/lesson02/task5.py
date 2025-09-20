def get_gcd(num1: int, num2: int) -> int:
    maxi = max(num1,num2)
    mini = min(num1,num2)
    ost = maxi%mini
    while(ost!=0):
        maxi = mini
        mini = ost
        ost = maxi%mini
    else:
        num1 = mini
    return num1