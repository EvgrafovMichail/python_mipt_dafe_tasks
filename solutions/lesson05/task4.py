def unzip(compress_text: str) -> str:
    list = compress_text.split()
    otv = ""
    for s in list:
        for i in range(len(s)):
            if s[i] == "*":
                otv += s[:i] * int(s[i + 1 :])
                break
        else:
            otv += s
    return otv
