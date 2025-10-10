def get_nth_digit(num):
    cnt_of_nums = 0
    digit_sum = 5

    if num <= digit_sum:
        return (num - 1) * 2

    while num > digit_sum:
        digit_sum += 45 * (10**cnt_of_nums) * (cnt_of_nums + 2)
        cnt_of_nums += 1

    k = num - (digit_sum - 45 * (10 ** (cnt_of_nums - 1)) * (cnt_of_nums + 1)) - 1
    k1 = k // (cnt_of_nums + 1)

    out_humber = 10**cnt_of_nums + k1 * 2

    return (out_humber // (10 ** ((cnt_of_nums) - (k % (cnt_of_nums + 1))))) % 10
