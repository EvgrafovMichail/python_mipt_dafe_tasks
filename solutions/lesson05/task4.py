def unzip(compress_text: str) -> str:
    result = ""
    buffer = ""
    i = 0
    lenght = len(compress_text)
    while True:
        if i + 1 > lenght:
            result += buffer
            break

        if compress_text[i] == "*":
            i += 1

            num_buffer = ""
            while i < lenght and compress_text[i].isdigit():
                num_buffer += compress_text[i]
                i += 1

            result += buffer * int(num_buffer)
            buffer = ""
            continue

        if compress_text[i].isspace():
            result += buffer
            buffer = ""
            i += 1
            continue

        buffer += compress_text[i]
        i += 1

    return result
