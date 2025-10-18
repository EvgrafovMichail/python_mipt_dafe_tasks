def are_anagrams(word1: str, word2: str) -> bool:
    if len(word2)!=len(word1):
        return False
    a = [0]*58
    for i in word1:
        a[ord(i)-65]+=1
    for i in word2:
        if a[ord(i)-65]==0:
            return False
        a[ord(i)-65]-=1
    return True
