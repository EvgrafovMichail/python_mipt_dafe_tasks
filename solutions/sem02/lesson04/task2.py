import numpy as np


def get_dominant_color_info(
    image: np.ndarray[np.uint8],
    threshold: int = 5,
) -> tuple[np.uint8, float]:
    if threshold < 1:
        raise ValueError("threshold must be positive")

    img = image.astype(np.int64)
    uniq, counts = np.unique(img, return_counts=True)
    delta = uniq[:, np.newaxis] - uniq
    res = np.abs(delta) < threshold
    result = np.sum(res * counts, axis=1)
    index = np.argmax(result)

    color = uniq[index]
    percentage = result[index] / image.size

    return np.uint8(color), float(percentage)
