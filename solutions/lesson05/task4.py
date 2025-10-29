def unzip(compress_text: str) -> str:
    compress_text = compress_text + " "
    new_str = ""
    user = ""
    mnogitel = ""
    for char in compress_text:
        if char in "1234567890":
            mnogitel += char
        elif char == " ":
            if len(mnogitel)>0:
                new_str += user*int(mnogitel)
                mnogitel = ""
            else:
                new_str += user
            user=""
        elif char != "*":
            user+=char
    compress_text = new_str
    return compress_text