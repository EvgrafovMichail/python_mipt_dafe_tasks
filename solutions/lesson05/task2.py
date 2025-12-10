def are_anagrams(word1: str, word2: str) -> bool:
    if len(word1) != len(word2):
        return False
    for char in word1:
        if word2.count(char) != word1.count(char):
            return False
    return True 
