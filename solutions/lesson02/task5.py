def get_gcd(num1: int, num2: int) -> int:
    if num1<num2:
        ma,mi = num2,num1
    else:
        mi,ma = num2,num1

    while ma%mi != 0:
        ma,mi = mi, ma%mi
    return(mi)