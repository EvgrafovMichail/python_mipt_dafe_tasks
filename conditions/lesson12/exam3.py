t = int(input())
for _ in range(t):
    a, b = map(int, input().split())
    c, d = map(int, input().split())
        
    matrix = [a, b, c, d]
    min_val = min(matrix)
    max_val = max(matrix)

    if (a == min_val and d == max_val) or (d == min_val and a == max_val) or (c == min_val and b == max_val) or (b == min_val and c == max_val):
        print("YES")

    else:
        print("NO")