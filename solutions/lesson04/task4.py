def move_zeros_to_end(nums: list[int]) -> list[int]:
    cnt_zero = nums.count(0)
    if cnt_zero == 0:
        return len(nums)
    elif cnt_zero == len(nums):
        return 0

    for elem in nums:
        if elem == 0:
            nums.remove(0)
            nums.append(0)

    for index_zero in range(len(nums)):
        if nums[index_zero] == 0:
            return index_zero
