def unzip(compress_text: str) -> str:
    res = ''
    for i in compress_text.split():
        if '*' in i:
            b = i.split('*')
            res += b[0] * int(b[1])
        else:
            res += i
    return res