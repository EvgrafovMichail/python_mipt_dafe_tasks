def len_num(num):
    cnt = 0
    while num > 0:
        num //= 10
        cnt += 1
    return cnt

def is_palindrome(num):
    if num < 0: 
        return False
    n = len_num(num)
    while num > 0 and n > 0:
        if num // 10 ** (n - 1) % 10 != num % 10: 
            return False
        num //= 10
        n -= 2
    return True
