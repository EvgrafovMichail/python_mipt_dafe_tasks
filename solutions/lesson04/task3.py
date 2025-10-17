def find_single_number(nums: list[int]) -> int:
    if len(nums) < 2:
        return nums[0]
    nums_sort = sorted(nums)
    if len(nums) == 3:
        if nums_sort[1] - nums_sort[0] != 0:
            return nums_sort[0]
        else:
            return nums_sort[2]
    a = int(len(nums) - 3)
    fst_num = nums_sort[0]
    scnd_num = nums_sort[1]
    for i in range(0, a):
        if fst_num - scnd_num != 0:
            return fst_num
        else:
            fst_num = nums_sort[i + 2]
            scnd_num = nums_sort[i + 3]
    return nums_sort[-1]
