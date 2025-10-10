def get_nth_digit(num: int) -> int:
    length, first, count = 1, 0, 5

    while True:
        box = count * length

        if num > box:
            num -= box
            length += 1
            first = 10(length - 1)
            count = (9 * 10(length - 1)) // 2

        else:
            break

    i = (num - 1) // length
    number = first + (i * 2)
    left = (num - 1) % length
    ans = (number // (10 ** (length - left - 1))) % 10

    return ans
