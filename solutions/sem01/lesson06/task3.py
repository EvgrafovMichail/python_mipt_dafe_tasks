def is_there_any_good_subarray(
    nums: list[int],
    k: int,
) -> bool:
    dictionary = {0: -1}
    curr = 0
    for i in range(len(nums)):
        curr = (curr + nums[i]) % k
        if curr in dictionary:
            if i - dictionary[curr] >= 2:
                return True
        else:
            dictionary[curr] = i
    return False
