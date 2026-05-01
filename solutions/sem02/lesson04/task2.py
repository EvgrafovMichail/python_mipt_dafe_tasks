import numpy as np


def get_dominant_color_info(
    image: np.ndarray[np.uint8],
    threshold: int = 5,
) -> tuple[np.uint8, float]:
    if threshold < 1:
        raise ValueError("threshold must be positive")

    unique_colors, unique_colors_count = np.unique(image, return_counts=True)
    colors_count = np.zeros(256)
    colors_count[unique_colors] = unique_colors_count

    pixels_in_dominant_group = 0
    for color in unique_colors:
        left_color_border = max(0, int(color) - threshold + 1)
        right_color_border = min(255, int(color) + threshold - 1)

        pixels_in_current_group = np.sum(colors_count[left_color_border : right_color_border + 1])

        if pixels_in_current_group > pixels_in_dominant_group:
            pixels_in_dominant_group = pixels_in_current_group
            dominant_color = color

    return dominant_color, float(pixels_in_dominant_group / image.size * 100)
