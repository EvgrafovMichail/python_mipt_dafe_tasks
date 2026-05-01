import numpy as np


def get_dominant_color_info(
    image: np.ndarray[np.uint8],
    threshold: int = 5,
) -> tuple[np.uint8, float]:
    if threshold < 1:
        raise ValueError("threshold must be positive")

    unique_colors, unique_colors_cnt = np.unique(image, return_counts=True)
    array_count_colors = np.zeros(256)
    array_count_colors[unique_colors] = unique_colors_cnt

    dominant_color = -1
    dominant_group_size = 0

    for color in unique_colors:
        left_limit = max(0, int(color) - threshold + 1)
        right_limit = min(256, int(color) + threshold - 1)

        curr_group_size = np.sum(array_count_colors[left_limit : right_limit + 1])
        if curr_group_size > dominant_group_size:
            dominant_group_size = curr_group_size
            dominant_color = color

    return dominant_color, float(dominant_group_size / image.size * 100)
