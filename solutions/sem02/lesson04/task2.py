import numpy as np


def get_dominant_color_info(
    image: np.ndarray[np.uint8],
    threshold: int = 5,
) -> tuple[np.uint8, float]:
    if threshold < 1:
        raise ValueError("threshold must be positive")

    counts = np.zeros(256, dtype=int)
    np.add.at(counts, image.flatten(), 1)

    padded = np.zeros(256 + 2 * threshold, dtype=int)
    padded[threshold : threshold + 256] = counts

    S = np.zeros(padded.size + 1, dtype=int)
    S[1:] = np.cumsum(padded)

    window_size = 2 * threshold - 1
    left = np.arange(1, 257, dtype=int)
    right = left + window_size
    smoothed = S[right] - S[left]

    smoothed[counts == 0] = -1

    dominant = np.uint8(np.argmax(smoothed))
    ratio = float(smoothed[dominant] / image.size)

    return dominant, ratio
