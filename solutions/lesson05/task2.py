def are_anagrams(word1, word2):
    counts = [0] * 52
    for char in word1:
        counts[ord(char) - ord('A') if 'A' <= char <= 'Z' else 26 + (ord(char) - ord('a'))] += 1
    for char in word2:
        counts[ord(char) - ord('A') if 'A' <= char <= 'Z' else 26 + (ord(char) - ord('a'))] -= 1
    return not(any(counts))