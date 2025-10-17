def count_cycles(lis: list[int]) -> int:
    count = 0
    pos = [1] * len(lis)

    for i in range(len(lis)):
        if pos[i] == 1:
            j = i
            pos[j] = 0

            while True:
                j = lis[j]

                if pos[j] == 0:
                    count += 1
                    break

                pos[j] = 0

    return count
