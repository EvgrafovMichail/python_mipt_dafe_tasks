def move_zeros_to_end(nums: list[int]) -> list[int]:
    cnt = nums.count(0)
    lt = 0
    rt = 0
    while rt < len(nums) - 1 and lt < len(nums) - 1:
        while nums[lt] != 0 and lt < len(nums) - 1:
            lt += 1
        if rt <= lt and lt < len(nums) - 1:
            rt = lt + 1
        while nums[rt] == 0 and rt < len(nums) - 1:
            rt += 1
        if nums[lt] == 0:
            nums[lt], nums[rt] = nums[rt], nums[lt]
    return len(nums) - cnt
