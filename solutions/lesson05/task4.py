def unzip(compress_text: str) -> str:
    compress_text_lst = compress_text.split()
    c = []
    n = 1
    for i in range(0, len(compress_text_lst)):
        if compress_text_lst[i][-1].isdigit() == True:
            while compress_text_lst[i][-n] != "*":
                n += 1
            a = compress_text_lst[i][:-n]
            d = compress_text_lst[i][-n + 1 :]
            compress_text_lst[i] = int(d) * a
        c = c + [compress_text_lst[i]]
    razarchive = "".join(c)
    return razarchive
