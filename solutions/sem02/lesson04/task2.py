import numpy as np


def get_dominant_color_info(
    image: np.ndarray[np.uint8],
    threshold: int = 5,
) -> tuple[np.uint8, float]:
    if threshold < 1:
        raise ValueError("threshold must be positive")

    values, freq = np.unique(image.reshape(-1), return_counts=True)

    hist = np.zeros(256, dtype=np.int32)
    hist[values] = freq

    cumsum = np.zeros(257, dtype=np.int32)
    cumsum[1:] = np.cumsum(hist)

    v = np.arange(256)
    left = np.maximum(0, v - threshold + 1)
    right = np.minimum(256, v + threshold)

    counts = cumsum[right] - cumsum[left]
    counts[hist == 0] = -1

    best = np.argsort(counts)[-1]

    return np.uint8(best), counts[best] / image.size
