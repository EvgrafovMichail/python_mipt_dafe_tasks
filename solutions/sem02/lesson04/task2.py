import numpy as np


def get_dominant_color_info(
    image: np.ndarray[np.uint8],
    threshold: int = 5,
) -> tuple[np.uint8, float]:
    if threshold < 1:
        raise ValueError("threshold must be positive")

    pixels = image.flatten()
    counts = np.zeros(256, dtype=np.int64)
    for color in range(256):
        mask = pixels == color
        counts[color] = np.sum(mask)

    max_pixels = 0
    best_color = 0
    for color in range(256):
        if counts[color] != 0:
            low = max(0, color - threshold + 1)
            high = min(255, color + threshold - 1)
            pixels = np.sum(counts[low : high + 1])

            if pixels > max_pixels:
                max_pixels = pixels
                best_color = color

    return np.uint8(best_color), (max_pixels / pixels.size) * 100
