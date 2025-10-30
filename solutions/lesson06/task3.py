def is_there_any_good_subarray(
    nums: list[int],
    k: int,
) -> bool:
    s = 0
    for i in range(len(nums)-1):
        s = nums[i]
        for j in range(i+1, len(nums)):
            s = s + nums[j]
            if s%k == 0:
                return True    

    return False

print(is_there_any_good_subarray([0, 1, 0], 2))