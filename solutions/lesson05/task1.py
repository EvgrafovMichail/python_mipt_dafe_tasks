def is_palindrome(text: str) -> bool:
    k=-1
    v=1
    text=text.lower()
    for i in range(len(text)):
        if text[i]!=text[k]:
            return False
        k-=1
    return True
