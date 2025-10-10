def get_nth_digit(num: int) -> int:
    if num == 1: return 0
    current_num = 2
    current_length = 1
    while True:
        # Count num length
        current_num_2 = current_num
        while current_num_2 != 0:
            current_num_2 //= 10
            current_length += 1

        if current_length >= num:
            return current_num // (10 ** (current_length - num)) % 10

        current_num += 2
