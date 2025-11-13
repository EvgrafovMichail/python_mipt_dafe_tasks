def get_nth_digit(num: int) -> int:
    k = 1
    total_digits = 5
    while num > total_digits:
        num -= total_digits
        k += 1
        if k == 2:
            total_digits = 45 * 2
        else:
            total_digits = (9 * 10**(k-1) // 2) * k
    
    pos = num
    if k == 1:
        first = 0
    else:
        first = 10**(k-1)
    
    num_index = (pos - 1) // k
    digit_index = (pos - 1) % k
    number = first + 2 * num_index
    
    power = 10**(k - 1 - digit_index)
    digit = (number // power) % 10
    return digit
