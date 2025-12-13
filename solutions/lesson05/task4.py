def unzip(compress_text: str) -> str:
    ans = ""
    splitted = compress_text.split(" ")
    for i in range(len(splitted)):
        splitted[i] = splitted[i].split("*")
        if len(splitted[i]) == 2:
            splitted[i] = str(splitted[i][0]) * int(splitted[i][1])
        ans += "".join(splitted[i])
    return ans
