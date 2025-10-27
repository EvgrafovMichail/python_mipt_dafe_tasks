def move_zeros_to_end(nums: list[int]) -> list[int]:
    length = len(nums)
    pos = length
    if 0 not in nums:
        return pos
    while True:
        ind = nums.index(0)
        for i in range(ind, length):
            print(nums[i])
            if nums[i] != 0:
                break
        else:
            pos = ind
            break
        for j in range(ind, length):
            if nums[j] != 0:
                nums[ind], nums[j] = nums[j], nums[ind]
                ind = nums.index(0)
    return pos
