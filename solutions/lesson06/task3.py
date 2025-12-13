def is_there_any_good_subarray(
    nums: list[int],
    k: int,
) -> bool:
    # сразу убираем плохие списки чтобы не мучиться
    if len(nums) < 2:
        return False
    # будем делить числа на k остаток от деления запоминать и потом к нему прибавлять след число
    # если след остаток от деления повторяется с ЛЮБЫМ из предыдущих значит что разница между
    # ними кратна к
    # эту разницу будем проверять на длинну
    remains = {0: -1}
    virable = 0

    for i in range(len(nums)):
        virable = (virable + nums[i]) % k

        # проверка подмассива в целом и длинны между числами чтобы понять норм или нет
        if virable in remains:
            if i - remains[virable] > 1:
                return True
        # если подмассив не крутой то просто запоминаем остаток и идем дальше
        else:
            remains[virable] = i

    return False
