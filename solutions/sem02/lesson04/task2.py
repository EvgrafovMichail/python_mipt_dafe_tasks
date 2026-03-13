import numpy as np


def get_dominant_color_info(
    image: np.ndarray,
    threshold: int = 5,
) -> tuple[np.uint8, float]:
    if threshold < 1:
        raise ValueError("threshold must be positive")
    pixels = image.flatten()
    total_pixels = len(pixels)
    unique_colors = np.unique(pixels)

    max_count = 0
    best_color = None
    for color in unique_colors:
        count = np.sum(np.abs(pixels.astype(int) - int(color)) < threshold)
        if count > max_count:
            max_count = count
            best_color = color

    percentage = (max_count / total_pixels) * 100
    return np.uint8(best_color), percentage
