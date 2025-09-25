def is_palindrome(num: int) -> bool:
    num_reversed = 0
    num_origin = num
    maxi=0
    while num >= 10**maxi:
        maxi +=1
    for i in range(1, maxi+1):
        reminder = num_origin % 10
        power=maxi-i
        num_reversed += reminder * 10**power
        num_origin -= reminder
        num_origin /= 10
    num_origin =num
    return num_origin == num_reversed
