def unzip(compress_text: str) -> str:
    compress_text = compress_text.split()
    ans = ""
    for a in compress_text:
        a = a.split("*")
        if len(a) == 2:
            ans += a[0] * int(a[1])
        else:
            ans += "".join(a)
    return ans
