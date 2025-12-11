def is_there_any_good_subarray(
    nums: list[int],
    k: int,
) -> bool:
    d, curr = {0: 0}, 0
    for i in range(len(nums)):
        curr += nums[i]
        if curr % k in d:
            if i - d[curr % k] > 0:
                return True
        else:
            d[curr % k] = i + 1
    return False


if __name__ == "__main__":
    print(is_there_any_good_subarray([0, 0], 1))
