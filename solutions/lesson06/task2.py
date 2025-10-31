def get_len_of_longest_substring(text: str) -> int:
    processing = set()
    shift = 0
    result = 0

    for letter in range(len(text)):
        while text[letter] in processing:
            processing.remove(text[shift])
            shift += 1
        processing.add(text[letter])
        result = max(result, letter - shift + 1)

    return result
