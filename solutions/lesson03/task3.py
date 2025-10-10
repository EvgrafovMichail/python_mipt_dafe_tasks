def get_nth_digit(num: int) -> int:
    final = 0
    i = 2
    j = i
    while final // 10**(num-1) <= 0 :
        while final // 10**(j-1)>0:
            j += 1
        final = final + (2*(i-1)*10**(j-1))
        j += 1
        i += 1
    final = final // 10**(num-1)
    rider = final // 10
    final = final - (rider*10) 
    return final