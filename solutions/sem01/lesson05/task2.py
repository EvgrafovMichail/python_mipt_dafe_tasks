def are_anagrams(word1: str, word2: str) -> bool:
    return "".join(sorted(list(word1))) == "".join(sorted(list(word2)))
