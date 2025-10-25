def is_palindrome(text: str) -> bool:
    text = text.lower()
    len_str = len(text)

    for i in range(len_str // 2):
        if text[i] != text[len_str - i - 1]:
            return False

    return True
