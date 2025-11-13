def make_averager(n):
    ans = []

    def get_avg(value):
        ans.append(value)

        if len(ans) > n:
            ans.pop(0)

        return sum(ans) / len(ans)
    
    return get_avg