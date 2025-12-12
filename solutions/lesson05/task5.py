def reg_validator(reg_expr: str, text: str) -> bool:
    nums = "0123456789"
    letters = "qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM"
    pos = 0
    for i in range(len(reg_expr)):
        char = reg_expr[i]
        if char == "d":
            if pos >= len(text) or text[pos] not in nums:
                return False
            while pos < len(text) and text[pos] in nums:
                pos += 1
        elif char == "w":
            if pos >= len(text) or text[pos] not in letters:
                return False
            while pos < len(text) and text[pos] in letters:
                pos += 1
        elif char == "s":
            if pos >= len(text) or (text[pos] not in nums and text[pos] not in letters):
                return False
            while pos < len(text) and (text[pos] in nums or text[pos] in letters):
                pos += 1
        else:
            if pos >= len(text) or text[pos] != char:
                return False
            pos += 1
    return pos == len(text)
