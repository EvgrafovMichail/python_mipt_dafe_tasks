def length(n):
    length = 0
    while n > 0:
        n //= 10
        length += 1
    return length

def find_n_in_sequence(num: int) -> int:
    counter, n =  1, 0
    while num > 0:
        if n % 10**counter == 0 and n != 0:
            counter += 1
        num -= counter
        n += 2
    
    return n - 2

def get_nth_digit(num: int) -> int:
    digit_in_num = 0
    n = find_n_in_sequence(num)
    next_n = n
        
    while n == next_n:
        num -= 1
        digit_in_num += 1
        next_n = find_n_in_sequence(num)
        
    n = (n // 10**(length(n) - digit_in_num)) % 10
    return n
