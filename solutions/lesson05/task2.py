def are_anagrams(word1: str, word2: str) -> bool:
    if len(word1) != len(word2):
        return False
    alphabet = {key : 0 for key in 'QWERTYUIOPASDFGHJKLZXCVBNMqwertyuiopasdfghjklzxcvbnm'}
    for char in word1:
        alphabet[char] += 1
    for char in word2:
        alphabet[char] -= 1
        if alphabet[char] < 0:
            return False
    return True