def is_there_any_good_subarray(
    nums: list[int],
    k: int,
) -> bool:
    for i in range(len(nums)):
        for j in range(i, len(nums)):
            if i != j:
                if sum(nums[i:j+1]) % k == 0:
                    return True
    return False
