def len_num(n):
    k = 0
    while n > 0:
        n //= 10
        k += 1
    return k

def get_nth_digit(n: int) -> int:

    i = 1
    flag = False
    
    if n == 1: 
        return 0
    
    for x in range(0, 10**10 , 2):
        if flag == False:
            k = len_num(x)
            r = None
            while k > 0:
                i += 1
                r = x // 10 ** (k - 1) % 10
                k -= 1
                if i == n:
                    flag = True
                    return r
        else:
            break

















