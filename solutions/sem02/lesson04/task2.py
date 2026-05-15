import numpy as np


def get_dominant_color_info(
    image: np.ndarray[np.uint8],
    threshold: int = 5,
) -> tuple[np.uint8, float]:

    if threshold < 1:
        raise ValueError

    max_count = -1
    often_color = 0
    image_int = image.astype(int)

    for color in range(256):
        check_mask = image == color
        if not np.any(check_mask):
            continue

        count_color = np.sum((np.abs(image_int - color)) < threshold)

        if count_color > max_count:
            max_count = count_color
            often_color = color

    procent = max_count / image.size

    return (np.uint8(often_color), float(procent))
