def count_cycles(arr: list[int]) -> int:
    checkpoint = 0
    proc = 0
    n = 0
    pos = []
    for i in range(len(arr)+1):
        if pos.count(i) == 0:
            checkpoint = arr[i]
            proc = arr[checkpoint]
            pos.append(checkpoint)
            while proc != checkpoint:
                proc = arr[proc]
                pos.append(proc)
            n += 1
            proc = 0
            checkpoint = 0
    return n