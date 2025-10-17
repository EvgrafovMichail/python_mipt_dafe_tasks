def move_zeros_to_end(nums: list[int]) -> list[int]:
    cnt = nums.count(0)
    l = 0
    r = 0

    while r < len(nums) - 1 and l < len(nums) - 1: 

        while nums[l] != 0 and l < len(nums) - 1:
            l += 1

        if r <= l and l < len(nums) - 1: 
            r = l + 1

        while nums[r] == 0 and r < len(nums) - 1: 
            r += 1

        if nums[l] == 0:
            nums[l], nums[r] = nums[r], nums[l]

    return len(nums) - cnt

