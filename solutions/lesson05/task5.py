def reg_validator(reg_expr: str, text: str) -> bool:
    reg_pointer = 0
    text_pointer = 0

    while reg_pointer != len(reg_expr):
        if text_pointer == len(text):
            return False

        state = reg_expr[reg_pointer]
        character = text[text_pointer]

        if state == "d":
            if not character.isdigit():
                return False

            text_pointer += 1
            while text_pointer < len(text) and text[text_pointer].isdigit():
                text_pointer += 1

            reg_pointer += 1

        elif state == "w":
            if not character.isalpha():
                return False

            text_pointer += 1
            while text_pointer < len(text) and text[text_pointer].isalpha():
                text_pointer += 1

            reg_pointer += 1

        elif state == "s":
            if not character.isalnum():
                return False

            while text_pointer < len(text) and text[text_pointer].isalnum():
                text_pointer += 1

            reg_pointer += 1

        else:
            if character != state:
                return False
            text_pointer += 1
            reg_pointer += 1

    return text_pointer == len(text)


print(reg_validator("s-dw", "12d=3-456a"))
