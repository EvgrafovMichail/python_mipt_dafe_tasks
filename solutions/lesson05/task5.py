def reg_validator(reg_expr: str, text: str) -> bool:
    for ch in reg_expr:
        match ch:
            case "d":
                if not (text and text[0] in "0123456789"):
                    return False
                while text and text[0] in "0123456789":
                    text = text[1:]
            case "w":
                if not (text and (65 <= ord(text[0]) <= 90 or 97 <= ord(text[0]) <= 122)):
                    return False
                while text and (65 <= ord(text[0]) <= 90 or 97 <= ord(text[0]) <= 122):
                    text = text[1:]
            case "s":
                if not (
                    text
                    and (
                        text[0] in "0123456789"
                        or 65 <= ord(text[0]) <= 90
                        or 97 <= ord(text[0]) <= 122
                    )
                ):
                    return False
                while text and (
                    text[0] in "0123456789" or 65 <= ord(text[0]) <= 90 or 97 <= ord(text[0]) <= 122
                ):
                    text = text[1:]
            case q:
                if not (text and text[0] == q):
                    return False
                text = text[1:]
    return not text


if __name__ == "__main__":
    print(reg_validator("w", "hello123"))
