def get_len_of_longest_substring(text: str) -> int:
    sybtext = text[::-1]
    double = ""
    lenmax1 = 0
    lenmax2 = 0
    lenn = 0
    while len(text) > 0:
        for g in text:
            if g not in double:
                double += g
                lenn += 1
            else:
                break
        if lenn > lenmax1:
            lenmax1 = lenn
        text = text[lenn:]
        lenn = 0
        double = ""
    while len(sybtext) > 0:
        for g in sybtext:
            if g not in double:
                double += g
                lenn += 1
            else:
                break
        if lenn > lenmax2:
            lenmax2 = lenn
        sybtext = sybtext[lenn:]
        lenn = 0
        double = ""

    return max(lenmax1, lenmax2)
