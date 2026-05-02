import numpy as np


def get_dominant_color_info(
    image: np.ndarray[np.uint8],
    threshold: int = 5,
) -> tuple[np.uint8, float]:
    if threshold < 1:
        raise ValueError("threshold must be positive")

    counts = np.zeros(256, dtype=int)
    for pixel in image.ravel():
        counts[pixel] += 1

    res_color = 0
    max_count = 0

    for i in range(256):
        if counts[i] == 0:
            continue

        left = max(0, i - threshold + 1)
        right = min(255, i + threshold - 1)
        current_sum = 0

        for j in range(left, right + 1):
            current_sum += counts[j]

        if current_sum > max_count:
            max_count = current_sum
            res_color = i

        elif current_sum == max_count:
            if counts[i] > counts[res_color]:
                res_color = i

    all_pixels = image.shape[0] * image.shape[1]

    return np.uint8(res_color), float((max_count / all_pixels) * 100)
