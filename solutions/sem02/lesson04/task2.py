import numpy as np


def get_dominant_color_info(
    image: np.ndarray[np.uint8],
    threshold: int = 5,
) -> tuple[np.uint8, float]:
    if threshold < 1:
        raise ValueError("threshold must be positive")

    flat = image.ravel()

    if len(flat) == 0:
        return 0.0

    unique_colors = np.unique(flat)

    best_color = 0
    max_count = 0

    for color in unique_colors:
        lower = max(0, int(color) - threshold + 1)
        upper = min(255, int(color) + threshold - 1)

        count = np.sum((flat >= lower) & (flat <= upper))

        if count > max_count:
            max_count = count
            best_color = color

    percent = (max_count / len(flat)) * 100.0
    return best_color, percent
