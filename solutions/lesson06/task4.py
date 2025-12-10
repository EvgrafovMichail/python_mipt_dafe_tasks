def count_unique_words(text: str) -> int:
    d = {}
    lst = text.split(" ")

    for i in range(len(lst)):
        for j in lst[i]:
            if not j.isalnum():
                lst[i] = lst[i].replace(j, "")
        lst[i] = lst[i].lower()
        d[lst[i]] = 0

    if "" in d:
        d.pop("")

    return len(d)
