def unzip(compress_text: str) -> str:
    uncomp = ""
    parts = compress_text.split()
    for i in parts:
        N = len(i)
        j = 0
        while j < N:
            if i[j] == "*":
                ch = int(i[j + 1 : N])
                uncomp += i[0:j] * ch
                break
            if j == N - 1:
                uncomp += i
            j += 1
    return uncomp


print(unzip("a*10"))
