def move_zeros_to_end(nums: list[int]) -> list[int]:
    ll = len(nums)
    i = 0
    k = 0
    while (ll-k) > i:
        if nums[i] == 0:
            k += 1
            nums.pop(i)
            nums.append(0)
        else:
            i += 1
    return ll-k  # я в принципе мог просто посчитать кол-во ноликов и вычесть
    # из длины(длина это O(1)), но пошел типа честным путем
