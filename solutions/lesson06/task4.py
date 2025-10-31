def count_unique_words(text: str) -> int:
    pun = "!.,\"'?-`;:()"
    text = text.lower()
    txt = ""
    for i in range(len(text)):
        if text[i] not in pun:
            txt += text[i]
    text = txt.split()
    dic = {}

    for i in range(len(text)):
        if text[i] not in dic and text[i] != "" and text[i] != " ":
            dic[text[i]] = i
        else:
            continue

    return len(dic)
