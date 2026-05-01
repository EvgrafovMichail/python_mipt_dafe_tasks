import numpy as np


def get_dominant_color_info(
    image: np.ndarray[np.uint8],
    threshold: int = 5,
) -> tuple[np.uint8, float]:
    if threshold < 1:
        raise ValueError("threshold must be positive")

    pixels = image.flatten()
    counts = np.zeros(256)
    for color in range(256):
        counts[color] = np.sum(pixels == color)

    result_color, result_count = 0, 0
    for color in range(256):
        if counts[color] == 0:
            continue
        min_with_threshold = max(0, color - (threshold - 1))
        max_with_threshold = min(255, color + (threshold - 1))
        count = np.sum(counts[min_with_threshold : max_with_threshold + 1])
        if count > result_count:
            result_count = count
            result_color = color

    return np.uint8(result_color), result_count / pixels.size * 100
