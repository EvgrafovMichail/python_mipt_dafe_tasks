def is_palindrome(text: str) -> bool:
    text =text.lower()
    for i in range(0, len(text)):
        if text[i] != text[len(text)-i-1]:
            return False
    return True