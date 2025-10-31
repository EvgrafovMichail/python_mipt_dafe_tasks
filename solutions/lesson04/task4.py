def move_zeros_to_end(nums: list[int]) -> list[int]:
    flag = False
    for i in range(len(nums)):
        if nums[i] == 0:
            del nums[i]
            nums.append(0)
            flag = True
    if flag:
        return nums.index(0)
    else:
        return len(nums)
