def flip_bits_in_range(num: int, left_bit: int, right_bit: int) -> int:
    answer = 0
    position = 1
    curr_bit = 1
    while num > 0:
        if curr_bit >= left_bit and curr_bit <= right_bit:
            if num % 2 == 1:
                answer = answer + position * 0
            else:
                answer = answer + position * 1
        else:
            answer = answer + position * (num % 2)
        position *= 10
        num //= 2
        curr_bit += 1
    while curr_bit <= right_bit:
        answer = answer + position * 1
        position *= 10
        curr_bit += 1
    num = 0
    power = 0
    while answer > 0:
        digit = answer % 10
        num += digit * (2**power)
        answer //= 10
        power += 1
    return num
