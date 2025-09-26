def is_palindrome(num: int) -> bool:
    num_reversed = 0
    num_origin = num
    if (num > 0) :
        numabc = num
    if (num < 0) :
        return False
    if (num == 0):
        numabc=0
    while(numabc>0) :
        num_reversed=num_reversed*10+numabc%10
        numabc=int((numabc-numabc%10)/10)
    if (num == 0):
        num_reversed = 0
    return num_origin == num_reversed

print(is_palindrome(-1))