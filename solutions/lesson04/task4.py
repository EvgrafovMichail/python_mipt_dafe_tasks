def move_zeros_to_end(nums: list[int]) -> list[int]:
    if all(nums[i] == 0 for i in range(len(nums))):
        return 0
    if all(nums[i] != 0 for i in range(len(nums))):
        return len(nums)
    divisors_lst = list()
    zero_lst = list()
    for i in range(len(nums)):
        if nums[i] == 0:
            zero_lst.append(nums[i])
        if nums[i] != 0:
            divisors_lst.append(nums[i])
    nums[:] = divisors_lst + zero_lst
    return nums.index(0)
