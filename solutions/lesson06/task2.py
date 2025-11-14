def get_len_of_longest_substring(text: str) -> int:
    n = len(text)
    max_lengths_list = []
    for i in range(n):
        current_set = set()
        for j in range(i, n):
            current_letter = text[j]

            if current_letter not in current_set:
                current_set.add(current_letter)

            else:
                unique_length = len(current_set)
                max_lengths_list.append(unique_length)
                break
        else:
            max_lengths_list.append(len(current_set))
    if not max_lengths_list:
        return 0
    return max(max_lengths_list)
