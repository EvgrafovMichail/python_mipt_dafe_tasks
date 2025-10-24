def are_anagrams(word1: str, word2: str) -> bool:
    
    if len(word1) != len(word2):
        return False
    
    if sorted(list(word1)) == sorted(list(word2)):
        return True
    else:
        return False