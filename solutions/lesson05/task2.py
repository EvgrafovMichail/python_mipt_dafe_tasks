def are_anagrams(word1: str, word2: str) -> bool:
    c = 0
    for i in range(len(word1)):
        if word1[i] in word2:
            word2 = word2.replace(word1[i], "", 1)
            c += 1
    if c == len(word1) and word2 == "":
        return True
    else:
        return False
