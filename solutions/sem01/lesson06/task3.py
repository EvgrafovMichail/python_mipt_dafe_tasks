def is_there_any_good_subarray(
    nums: list[int],
    k: int,
) -> bool:
    remainder_index = {0: -1}
    prefix_sum = 0

    for i, num in enumerate(nums):
        prefix_sum = (prefix_sum + num) % k

        if prefix_sum in remainder_index:
            if i - remainder_index[prefix_sum] >= 2:
                return True
        else:
            remainder_index[prefix_sum] = i

    return False
