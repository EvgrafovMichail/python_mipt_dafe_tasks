def are_anagrams(word1: str, word2: str) -> bool:
    a = [0] * 58
    for i in word1:
        a[ord(i) - 65] += 1
    for i in word2:
        a[ord(i) - 65] -= 1
    return all(x == 0 for x in a)
