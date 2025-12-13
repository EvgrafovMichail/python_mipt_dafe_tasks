def unzip(compress_text: str) -> str:
    res = []
    for t in compress_text.split():
        if "*" in t:
            s, n = t.split("*")
            res.append(s * int(n))
        else:
            res.append(t)
    return "".join(res)
