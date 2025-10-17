def merge_intervals(intervals: list[list[int, int]]) -> list[list[int, int]]:
    rezs = []
    if not intervals: return rezs
    allhours = []
    ends = []

    for lis in intervals:
        newl = list(range(lis[0], lis[1] + 1))

        for end in ends:
            if lis[0] < end < lis[1]:
                ends.remove(end)

        if min(lis) != 0 and min(lis) not in allhours: 
            ends.append(min(lis) - 0.5)

        for hour in newl:
            if hour not in allhours:
                allhours.append(hour)

    print(ends)
    podposl = []
    print(sorted(allhours))

    for hour in range(0, max(allhours) + 1):
        if hour in allhours and hour == max(allhours):
            rezs.append(podposl + [hour])

        elif podposl:
            if hour not in allhours:
                podposl.append(hour - 1)
                rezs.append(podposl)
                podposl = []

            elif (hour + 0.5) in ends:
                podposl.append(hour)
                rezs.append(podposl)
                podposl = []

        elif hour in allhours and not podposl:
            podposl.append(hour)

    return rezs
