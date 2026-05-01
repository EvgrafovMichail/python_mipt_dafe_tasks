import numpy as np


def get_dominant_color_info(
    image: np.ndarray[np.uint8],
    threshold: int = 5,
) -> tuple[np.uint8, float]:
    if threshold < 1:
        raise ValueError

    pixels = image.flatten()
    zerose = np.zeros(256, dtype=np.int64)
    for color in range(256):
        mask = pixels == color
        zerose[color] = np.sum(mask)

    max_pixels = 0
    best_color = 0
    for current_color in range(256):
        if zerose[current_color] != 0:
            left = max(0, current_color - (threshold - 1))
            right = min(255, current_color + (threshold - 1))
            current_sum = np.sum(zerose[left : right + 1])

            if current_sum > max_pixels:
                max_pixels = current_sum
                best_color = current_color

    percent = (max_pixels / pixels.size) * 100
    return np.uint8(best_color), float(percent)