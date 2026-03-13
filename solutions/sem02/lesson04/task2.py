import numpy as np


def get_dominant_color_info(
    image: np.ndarray[np.uint8],
    threshold: int = 5,
) -> tuple[np.uint8, float]:
    if threshold < 1:
        raise ValueError("threshold must be positive")
    pixels = np.sort(image.flatten())
    max_color = 0
    max_count = 0
    left = 0
    center = 0
    for right in range(len(pixels)):
        while pixels[right] - pixels[center] >= threshold:
            center += 1
        while pixels[center] - pixels[left] >= threshold:
            left += 1
        if right - left + 1 > max_count:
            max_count = right - left + 1
            max_color = pixels[center]
    return max_color, max_count * 100 / len(pixels)
