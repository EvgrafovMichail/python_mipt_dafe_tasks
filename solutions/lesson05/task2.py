def are_anagrams(word1: str, word2: str) -> bool:
    t = True
    if len(word1) != len(word2):
        t = False

    lst = [0] * ord("z")
    for i in word1:
        lst[ord(i)] += 1
    for i in word2:
        lst[ord(i)] -= 1
        if lst[ord(i)] < 0:
            t = False
    return t
