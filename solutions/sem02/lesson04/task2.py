import numpy as np


def get_dominant_color_info(
    image: np.ndarray,
    threshold: int = 5,
) -> tuple[np.uint8, float]:
    if threshold < 1:
        raise ValueError('threshold must be positive')

    first, second = image.shape
    total = first * second
    if total == 0:
        return (np.uint8(0), 0.0)

    num = [0] * 256
    for i in range(first):
        for j in range(second):
            num[image[i, j]] += 1

    palette = [i for i in range(256) if num[i] > 0]
    if not palette:
        return (np.uint8(0), 0.0)
    if len(palette) == 1:
        return (np.uint8(palette[0]), 100.0)

    biggest_sum = -1
    most_frequent_col = 0
    for c in palette:
        low = max(0, c - threshold + 1)
        high = min(255, c + threshold - 1)
        s = 0
        for k in range(low, high + 1):
            s += num[k]
        if s > biggest_sum:
            biggest_sum = s
            most_frequent_col = c

    percentage = (biggest_sum / total) * 100.0
    return (np.uint8(most_frequent_col), percentage)
