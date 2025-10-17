def get_nth_digit(num: int) -> int:
    length = 1

    while True:
        if length == 1:
            first_in_group = 0
        else:
            first_in_group = 10 ** (length - 1)
        amount = (10**length - first_in_group) // 2 * length

        if amount >= num:
            pos_in_num = (num - 1) % length
            in_number = first_in_group + ((num - 1) // length) * 2

            while in_number >= 0:
                length -= 1

                if pos_in_num == length:
                    return in_number % 10
                in_number = in_number // 10
        length += 1
        num -= amount
