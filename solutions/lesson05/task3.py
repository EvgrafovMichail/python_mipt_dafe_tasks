def is_punctuation(text: str) -> bool:
    if len(text)==0:
        return False
    punctuation_marks =  "!#$%&'()*+,-./:;<=>?@[\]^_{|}~`\""
    for char in text:
        if  (char  not in punctuation_marks):
            return False
    return True
