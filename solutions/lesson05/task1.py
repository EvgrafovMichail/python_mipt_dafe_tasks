def is_palindrome(text: str) -> bool:
    begin, end = 0, len(text) - 1

    while end - begin > 0:
        if text[begin].lower() != text[end].lower():
            return False
        begin, end = begin + 1, end - 1

    return True
