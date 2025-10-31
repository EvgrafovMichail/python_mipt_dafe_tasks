def is_there_any_good_subarray(
    nums: list[int],
    k: int,
) -> bool:
    n = len(nums)

    sum = [0] * (n + 1)

    for i in range(n):
        sum[i + 1] = sum[i] + nums[i]

    for i in range(n):
        for j in range(i + 1, n):
            divisible_sum = sum[j + 1] - sum[i]
            if divisible_sum % k == 0:
                return True

    return False
