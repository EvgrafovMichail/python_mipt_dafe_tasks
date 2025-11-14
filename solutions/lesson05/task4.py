def unzip(compress_text: str) -> str:
    ans = ""
    for i in compress_text.split():
        words = ""
        fl = False
        kol = ""
        for j in i:
            if j == "*":
                fl = True
                continue
            if fl:
                kol += j
            else:
                words += j
        if kol:
            ans += words * int(kol)
        else:
            ans += words
    return ans
