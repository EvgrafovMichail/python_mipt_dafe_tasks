import numpy as np


def get_dominant_color_info(
    image: np.ndarray[np.uint8],
    threshold: int = 5,
) -> tuple[np.uint8, float]:
    if threshold < 1:
        raise ValueError("threshold must be positive")
    p = image.flatten()
    c = [np.sum(p == i) for i in range(256)]
    m, b = 0, 0
    for i in range(256):
        if c[i]:
            s = sum(c[max(0, i - threshold + 1) : min(256, i + threshold)])
            if s > m:
                m, b = s, i
    return np.uint8(b), float(m / len(p) * 100)
