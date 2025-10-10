def length(num: int):
    ans = 0
    if num == 0:
        return 1
    while num != 0:
        num = num // 10
        ans += 1
    return ans


def get_nth_digit(num: int) -> int:
    digits = 0
    sequence = 0
    ans = 0
    if num < 6:
        return num * 2 - 2
    while 1:
        digits += length(sequence)

        if digits >= num:
            sequence = sequence // (10 ** (digits - num))
            ans = sequence % 10
            return ans

        sequence += 2
