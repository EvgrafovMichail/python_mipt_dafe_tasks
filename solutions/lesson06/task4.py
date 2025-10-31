def count_unique_words(text: str) -> int:
    s = set()
    text = text.lower()
    curword = ""
    for i in range(len(text)):
        c = text[i]
        if c == " ":
            if len(curword) > 0:
                s.add(curword)
                curword = ""
            continue
        j = ord(c)
        if not (33 <= j <= 47 or 58 <= j <= 64 or 91 <= j <= 96 or 123 <= j <= 126):
            curword += c
    if len(curword) > 0:
        s.add(curword)
    # ваш код
    return len(s)
