def is_palindrome(text: str) -> bool:
    if not text:
        return True

    str_low = text.lower()
    if str_low[0] == str_low[-1]:
        return True
    else:
        return False


# print(is_palindrome(input("Введите палиндром ")))
