def unzip(compress_text: str) -> str:
    # ваш код
    res_text = []
    i = 0
    length = len(compress_text)

    while i < length:
        if compress_text[i] == " ":
            i += 1
            continue

        j = i
        while j < length and compress_text[j] != "*" and compress_text[j] != " ":
            j += 1

        text_block = compress_text[i:j]

        if j < length and compress_text[j] == "*":
            k = j + 1
            while k < length and compress_text[k].isdigit():
                k += 1

            count = int(compress_text[j + 1 : k]) if k > j + 1 else 1

            res_text.append(text_block * count)
            i = k
        else:
            res_text.append(text_block)
            i = j

    compress_text = "".join(res_text)

    return compress_text
