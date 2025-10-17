def get_kolvo_num(n):
    if n == 0:
        return 1
    count = 0
    while n > 0:
        count += 1
        n //= 10
    return count


def get_nth_digit(num: int) -> int:
    ct = 0
    for i in range(0, num + 1, 2):
        ct += get_kolvo_num(i)
    return num
