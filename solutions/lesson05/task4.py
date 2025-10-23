def unzip(compress_text: str) -> str:
    f = 0
    s = ""
    repeat = ""
    num = ""
    for i in compress_text:
        if i == " ":
            if f == 1:
                s += repeat * int(num)
                f = 0
                num = ""
            else:
                s += repeat
            repeat = ""
        if 65 <= ord(i) <= 90 or 97 <= ord(i) <= 122:
            repeat += i
        if 48 <= ord(i) <= 57:
            num += i
        if i == "*":
            f = 1
    if repeat != "":
        if num != "":
            s += repeat * int(num)
        else:
            s += repeat

    return s
