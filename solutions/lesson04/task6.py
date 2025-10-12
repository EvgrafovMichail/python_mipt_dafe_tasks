def count_cycles(arr: list[int]) -> int: 
    if not arr:
        return 0
    
    n = len(arr)
    visited = [False] * n
    cycle_count = 0
    
    for i in range(n):
        if not visited[i]:
            current = i
            while not visited[current]:
                visited[current] = True
                current = arr[current]
            cycle_count += 1
    
    return cycle_count