def unzip(compress_text: str) -> str:
    decompress_text = ""
    new_text = compress_text.split()
    for i in new_text:
        match i.split('*'):
            case [text, num]:
                decompress_text=decompress_text+text*int(num)
            case [text]:
                decompress_text=decompress_text+text
    return decompress_text
