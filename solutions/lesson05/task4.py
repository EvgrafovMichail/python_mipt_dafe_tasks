def unzip(compress_text: str) -> str:
    # ваш код
    els = compress_text.split()
    compress_text_reskin = []
    for el in els:
        if "*" in el:
            text, num = el.split("*")
            compress_text_reskin.append(text * int(num))
        else:
            compress_text_reskin.append(el)
    compress_text_reskin = "".join(compress_text_reskin)
    return compress_text_reskin
