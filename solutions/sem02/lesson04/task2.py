import numpy as np


def get_dominant_color_info(
    image: np.ndarray[np.uint8],
    threshold: int = 5,
) -> tuple[np.uint8, float]:
    if threshold < 1:
        raise ValueError("threshold must be positive")

    if image.size == 0:
        return np.uint8(0), 0.0

    uniq, counts = np.unique(image, return_counts=True)
    color_freq = np.zeros(256)
    color_freq[uniq] = counts

    prefix_sum = np.zeros(257)
    prefix_sum[1:] = np.cumsum(color_freq)

    index_array = np.arange(256)
    left_indexes = np.clip(index_array - threshold + 1, 0, 255)
    right_indexes = np.clip(index_array + threshold - 1, 0, 255)

    window_sums = prefix_sum[right_indexes + 1] - prefix_sum[left_indexes]
    window_sums[color_freq == 0] = -1

    best_color = np.argmax(window_sums)
    best_sum = window_sums[best_color]
    percent = best_sum / image.size * 100

    return np.uint8(best_color), percent
