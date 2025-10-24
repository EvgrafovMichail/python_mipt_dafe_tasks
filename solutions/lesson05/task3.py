def is_punctuation(text: str) -> bool:
    if len(text) == 0:
        return False
    else:
        text_lst = list(text)
        a = 0
        for i in range(0, len(text_lst)):
            if not text[i].isalnum() and not text[i].isspace():
                a += 1
            else:
                return False
        if a == len(text):
            return True
