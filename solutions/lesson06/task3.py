def is_there_any_good_subarray(
    nums: list[int],
    k: int,
) -> bool:
    n = len(nums)
    if n < 2:
        return False

    sums = [0] * n

    for i in range(n):
        sums[i] = nums[i] + sums[i - 1]

    mods = {sums[0] % k: 0}

    for i in range(1, n):
        cur_mod = sums[i] % k

        if cur_mod == 0:
            return True

        if cur_mod in mods:
            begin, end = mods[cur_mod], i

            if end - begin > 1:
                return True

        else:
            mods[cur_mod] = i

    return False


arr = [i for i in range(1000)]

for i in range(1, 10000):
    is_there_any_good_subarray(arr, i)
