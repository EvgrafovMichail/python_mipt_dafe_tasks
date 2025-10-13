def count_cycles(arr: list[int]) -> int: 
    cnt = 0
    used_i = []
    for i in range(len(arr)):   
        if i in used_i:
            cnt +=0
        elif arr[i]==i:
            cnt +=1
        else:
            j = i
            used_i.append(arr[j])
            while arr[j]!=i:
                j = arr[j]
                used_i.append(arr[j])
            cnt +=1
    return cnt