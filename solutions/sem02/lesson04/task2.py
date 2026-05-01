import numpy as np


def get_dominant_color_info(
    image: np.ndarray[np.uint8],
    threshold: int,
) -> tuple[np.uint8, float]:
    if threshold < 1:
        raise ValueError("threshold must be positive")

    fr = np.bincount(image.reshape(-1))
    colors = np.where(fr > 0)[0]
    counts = np.zeros(256, dtype=np.int64)

    for i in colors:
        low = max(0, i - threshold + 1)
        high = min(255, i + threshold - 1)
        counts[i] = np.sum(fr[low : high + 1])

    return np.uint8(np.argmax(counts)), float(np.max(counts) / image.size)
