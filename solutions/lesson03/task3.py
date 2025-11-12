def get_nth_digit(num: int):
    if num == 0:
        return 0
    else:
        num -= 1
        n = num
        d = 1

        while True:
            start = 10 ** (d - 1)
            if start % 2 != 0:
                start += 1
            end = 10**d - 1
            if end % 2 != 0:
                end -= 1

            if start <= end:
                count_numbers = ((end - start) // 2) + 1
                total_digits = count_numbers * d
            else:
                total_digits = 0

            if n <= total_digits:
                index_in_group = (n - 1) // d
                left = (n - 1) % d
                target_number = start + index_in_group * 2

                p = d - 1 - left
                power = 1
                for _ in range(p):
                    power *= 10
                digit = (target_number // power) % 10

                # right = d - left - 1

                # print(target_number)
                # print(left)
                # print(right)
                # print(digit)
                return digit
            else:
                n -= total_digits
                d += 1
