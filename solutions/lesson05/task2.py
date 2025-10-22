def are_anagrams(word1: str, word2: str) -> bool:
    a = True

    for i in word1:
        if not (i in word1):
            a = False

    for i in word2:
        if not (i in word1):
            a = False

    return a
