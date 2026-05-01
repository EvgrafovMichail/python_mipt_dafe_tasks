def unzip(compress_text: str) -> str:
    # ваш код
    parts = compress_text.split()
    result = []
    for part in parts:
        if "*" in part:
            base, num_str = part.split("*", 1)
            try:
                n = int(num_str)
            except ValueError:
                n = 0
            result.append(base * n)
        else:
            result.append(part)
    return "".join(result)
