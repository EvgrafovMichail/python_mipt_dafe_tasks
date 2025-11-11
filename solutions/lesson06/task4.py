def count_unique_words(text: str) -> int:
    punctuation = "!\"#$%&'()*+,-./:;<=>?@[\\]^_`{|}~"

    words = set()
    current_word = ""

    for char in text + " ":
        if char.isspace():
            if current_word:
                left = 0
                right = len(current_word) - 1

                while left <= right and current_word[left] in punctuation:
                    left += 1
                while right >= left and current_word[right] in punctuation:
                    right -= 1

                if left <= right:
                    words.add(current_word[left : right + 1].lower())

                current_word = ""
        else:
            current_word += char

    return len(words)
