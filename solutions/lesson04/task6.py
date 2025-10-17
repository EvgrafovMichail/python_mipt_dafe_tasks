def count_cycles(arr: list[int]) -> int: 
    cycle = 0
    for i in range(len(arr)):
        if arr[i] != -1:
            cycle += 1
        
            element = arr[i]
            while arr[element] != -1:
                remember = arr[element]
                arr[element] = -1
                element=remember
        
    return cycle
