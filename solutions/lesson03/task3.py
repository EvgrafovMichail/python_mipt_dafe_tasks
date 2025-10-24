def get_nth_digit(num: int) -> int:
    if num == 1:
        return 0

    num -= 1
    digit_count = 1

    while True:
        if digit_count == 1:
            numbers_count = 4
        else:
            numbers_count = 4 * (10 ** (digit_count - 1))

        total_digits = numbers_count * digit_count

        if num > total_digits:
            num -= total_digits
            digit_count += 1
        else:
            number_index = (num - 1) // digit_count
            digit_position = (num - 1) % digit_count

            first_number = 10 ** (digit_count - 1)
            if first_number % 2 != 0:
                first_number += 1

            number = first_number + 2 * number_index

            divisor = 10 ** (digit_count - digit_position - 1)
            digit = (number // divisor) % 10

            return digit
