def unzip(compress_text: str) -> str:
    res = ""
    temp = ""
    num = ""
    for i in compress_text:
        if i.isdigit():
            num += i
        else:
            if num:
                res += temp * int(num)
                num = ""
                temp = ""
            else:
                if i == " ":
                    res += temp
                    temp = ""
                else:
                    if i != "*":
                        temp += i
    if num:
        res += temp * int(num)
    else:
        res += temp

    return res
