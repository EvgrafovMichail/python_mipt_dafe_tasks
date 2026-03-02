t = int(input())
for _ in range(t):
    n, k = map(int, input().split())
    lst = list(map(int, input().split()))
    lst.sort(reverse=True)
        
#   max_coins = max(lst)
    max_add = k
        
    for m in range(1, n + 1):
        if k % m == 0:
            x = k // m
            added = 0
            for i in range(min(m, n)):
                if lst[i] < x:
                    added += x - lst[i]
            max_add = min(max_add, added)
                
    print(max_add)

