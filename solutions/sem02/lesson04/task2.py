import numpy as np


def get_dominant_color_info(
    image: np.ndarray[np.uint8],
    threshold: int = 5,
) -> tuple[np.uint8, float]:

    if threshold < 1:
        raise ValueError("threshold must be positive")

    colors = [0] * 256

    for i in range(image.shape[0]):
        for j in range(image.shape[1]):
            colors[image[i, j]] += 1

    max_sum = 0
    dominant_color = -1
    for i in range(256):
        if colors[i] > 0:
            start = max(0, i - threshold + 1)
            end = min(255, i + threshold - 1)
            now_sum = sum(colors[start : end + 1])
            if now_sum > max_sum:
                max_sum = now_sum
                dominant_color = i

    return np.uint8(dominant_color), max_sum / (image.shape[0] * image.shape[1])
