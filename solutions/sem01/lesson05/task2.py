def are_anagrams(word1: str, word2: str) -> bool:
    low = [0] * 26
    up = [0] * 26
    for symbol in word1:
        if "a" <= symbol <= "z":
            low[ord(symbol) - ord("a")] += 1
        else:
            up[ord(symbol) - ord("A")] += 1
    for symbol in word2:
        if "a" <= symbol <= "z":
            low[ord(symbol) - ord("a")] -= 1
        else:
            up[ord(symbol) - ord("A")] -= 1
    return low == up == [0] * 26
