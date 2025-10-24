def move_zeros_to_end(nums: list[int]) -> list[int]:
    cnt = nums.count(0)
    left = 0
    right = 0

    while right < len(nums) - 1 and left < len(nums) - 1:
        while nums[left] != 0 and left < len(nums) - 1:
            left += 1

        if right <= left and left < len(nums) - 1:
            right = left + 1

        while nums[right] == 0 and right < len(nums) - 1:
            right += 1

        if nums[left] == 0:
            nums[left], nums[right] = nums[right], nums[left]

    return len(nums) - cnt
