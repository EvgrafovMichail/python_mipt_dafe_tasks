def are_anagrams(word1: str, word2: str) -> bool:
    if len(word1) != len(word2):
        return False

    counts = [0] * 52

    for char in word1:
        counts[ord(char) - (65 if char <= "Z" else 71)] += 1

    for char in word2:
        counts[ord(char) - (65 if char <= "Z" else 71)] -= 1

    for count in counts:
        if count != 0:
            return False
    return True
