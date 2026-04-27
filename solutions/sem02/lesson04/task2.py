import numpy as np


def get_dominant_color_info(
    image: np.ndarray[np.uint8],
    threshold: int = 5,
) -> tuple[np.uint8, float]:
    if threshold < 1:
        raise ValueError("threshold must be positive")

    pixels = image.flatten()
    zeros = np.zeros(256, dtype=np.int64)
    for pixel in pixels:
        zeros[pixel] += 1

    max_pixels = 0
    best_color = 0

    for current_color in range(256):
        if zeros[current_color] != 0:
            left = max(0, current_color - threshold + 1)
            right = min(255, current_color + threshold - 1)
            summa = np.sum(zeros[left : right + 1])

            if summa > max_pixels:
                max_pixels = summa
                best_color = current_color

    percent = (max_pixels / pixels.size) * 100

    return np.uint8(best_color), float(percent)
