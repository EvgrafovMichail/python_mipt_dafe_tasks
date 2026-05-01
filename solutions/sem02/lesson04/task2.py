import numpy as np


def get_dominant_color_info(image: np.ndarray, threshold: int) -> tuple[np.uint8, float]:
    if threshold < 1:
        raise ValueError("threshold must be positive")

    pixels = image.flatten()
    total_pixels = len(pixels)
    unique_colors = set(pixels)

    best_count = 0
    best_color = 0

    for color in unique_colors:
        count = np.sum(np.abs(pixels.astype(int) - color) < threshold)

        if count > best_count:
            best_count = count
            best_color = color
        elif count == best_count:
            if color < best_color:
                best_color = color

    percentes = best_count / total_pixels * 100
    return (np.uint8(best_color), percentes)
