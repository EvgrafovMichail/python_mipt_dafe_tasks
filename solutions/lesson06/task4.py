def count_unique_words(text: str) -> int:
    w = text.split()
    u = set()
    for x in w:
        c = x.lower()
        while c and not c[0].isalnum():
            c = c[1:]
        while c and not c[-1].isalnum():
            c = c[:-1]
        if c:
            u.add(c)
    return len(u)
