import numpy as np


def get_dominant_color_info(
    image: np.ndarray[np.uint8],
    threshold: int = 5,
) -> tuple[np.uint8, float]:
    if threshold < 1:
        raise ValueError("threshold must be positive")

    unique_pixels, pixel_counts = np.unique(image, return_counts=True)

    extended_pixel_counts = np.zeros(256)
    extended_pixel_counts[unique_pixels] = pixel_counts

    max_sum = 0

    for center in unique_pixels:
        left = max(0, int(center) - threshold + 1)
        right = min(255, int(center) + threshold - 1)
        current_sum = np.sum(extended_pixel_counts[left : right + 1])

        if current_sum > max_sum:
            max_sum = current_sum
            popular_color = center

    return popular_color, float(max_sum / image.size * 100)
