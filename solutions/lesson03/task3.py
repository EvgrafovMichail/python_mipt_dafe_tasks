# 1 2 3 4 5 6 7 8 9 A B C D E F
# 0 2 4 6 8 1 0 1 2 1 4 1 6 1 8 2 0

# 98 100 102

# 1зн [0, 10) = 10 * 1 // 2
# 2зн [10, 100) = 90 * 2 // 2
# 3зн [100, 1000) = 900 * 3 // 2
# 4зн [1000, 1000) = 9000 * 4 // 2
# 5зн [10000, 100000)  = 90000 * 5 // 2
# n зн = [10eN, 10e(N+1)) = 9e(N-1) * N // 2
    
# 12045 % 1000 = 045 // 100 = 0
# 54321 n = 3
    

def get_nth_digit(num: int) -> int:

    pos = num
    digit_count = 1
    
    begin, end = 0, 10
    
    while True:
        count = (end - begin) * digit_count // 2
 
        if pos - count < 0:
            break
        
        pos -= count 
        digit_count += 1
        begin = end
        end *= 10
    
    n_number = begin + ((pos + digit_count - 1) // digit_count - 1) * 2

    pos = ((pos + digit_count - 1) // digit_count) * digit_count - pos + 1

    return n_number % (10**pos) // (10**(pos - 1))