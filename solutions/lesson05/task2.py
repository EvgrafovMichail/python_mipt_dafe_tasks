def are_anagrams(word1: str, word2: str) -> bool:
    n = len(word1)
    m = len(word2)
    if m != n:
        return False
    ll = [0] * (123 - 65)
    for i in range(n):
        ll[ord(word1[i]) - 65] += 1
    for i in range(m):
        ll[ord(word2[i]) - 65] -= 1
        if ll[ord(word2[i]) - 65] < 0:
            return False
    return True
