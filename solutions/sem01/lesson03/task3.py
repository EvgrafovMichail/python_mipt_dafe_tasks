def get_nth_digit(num: int) -> int:
    if num <= 5:
        return (num - 1) * 2
    num -= 5
    rank = 2
    left = 10
    right = 100
    total_digits_so_far = 0
    while True:
        count = (right - left) // 2
        total_digits = count * rank

        if total_digits_so_far + total_digits < num:
            total_digits_so_far += total_digits
            rank += 1
            left = right
            right *= 10

        else:
            pos_in_rank = num - total_digits_so_far - 1
            number_index = pos_in_rank // rank
            digit_pos = pos_in_rank % rank
            number = left + number_index * 2

            for _ in range(rank - digit_pos - 1):
                number //= 10
            return number % 10
    return 0
