def unzip(comprtext: str) -> str:
    substrings = comprtext.split()
    for i in range(len(substrings)):
        if "*" in substrings[i]:
            string, count = substrings[i].split("*")
            substrings[i] = string * int(count)
    resultstring = "".join(substrings)
    return resultstring
