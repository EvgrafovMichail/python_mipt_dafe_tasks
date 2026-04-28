def merge_intervals(intervals: list[list[int, int]]) -> list[list[int, int]]:
    time = [0] * (10**6 + 1)
    for interval in intervals:
        time[interval[0]] += 1
        time[interval[1]] -= 1
    k = 0
    st = -1
    answer = []
    for i in range(0, 10**6 + 1):
        if time[i] > 0:
            k += time[i]
            if st == -1:
                st = i
        if time[i] < 0:
            k += time[i]
            if k == 0:
                answer.append([st, i])
                st = -1
    return answer


# алгоритм не оптимален для маленького количества интервалов
# но если их количество будет большим, то должен отлично подходить
