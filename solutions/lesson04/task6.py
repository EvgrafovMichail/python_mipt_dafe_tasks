def count_cycles(l: list[int]) -> int:
    count = 0
    pos = [1] * len(l)

    for i in range(len(l)):
        if pos[i] == 1:
            j = i
            pos[j] = 0

            while True:
                j = l[j]

                if pos[j] == 0:
                    count += 1
                    break

                pos[j] = 0

    return count
