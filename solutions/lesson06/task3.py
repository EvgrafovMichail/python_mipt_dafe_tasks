def is_there_any_good_subarray(
    nums: list[int],
    k: int,
) -> bool:
    # ваш код
    if len(nums) < 2:
        return False

    for num in range(len(nums)):
        nums[num] = nums[num] % k

    for num in range(len(nums) - 1):
        if nums[num] == 0 and nums[num + 1] == 0:
            return True
    left = 0
    current_sum = 0

    for right in range(len(nums)):
        current_sum += nums[right]
        while current_sum > k and left <= right:
            current_sum -= nums[left]
            left += 1
        if current_sum == k:
            return True
    return False
