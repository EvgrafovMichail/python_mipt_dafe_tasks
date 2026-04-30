import numpy as np


def get_dominant_color_info(
    image: np.ndarray,
    threshold: int = 5,
) -> tuple[np.uint8, float]:
    if threshold < 1:
        raise ValueError("threshold must be positive")

    image = image.ravel()
    counts = np.zeros(256, dtype=np.int64)

    for color in range(256):
        counts[color] = np.sum(image == color)

    cnt_colors = np.zeros(257, dtype=np.int64)
    cnt_colors[1:] = np.cumsum(counts)

    max_sum, color_for_ans = -1.0, 0

    for curr_color in range(256):
        if counts[curr_color] == 0:
            continue

        left = max(0, curr_color - threshold + 1)
        right = min(255, curr_color + threshold - 1)

        curr_sum = float(cnt_colors[right + 1] - cnt_colors[left])

        if curr_sum > max_sum:
            max_sum = curr_sum
            color_for_ans = curr_color

    return np.uint8(color_for_ans), (max_sum / image.size) * 100
