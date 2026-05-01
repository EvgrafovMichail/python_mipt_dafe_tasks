import numpy as np


def get_dominant_color_info(
    image: np.ndarray[np.uint8],
    threshold: int = 5,
) -> tuple[np.uint8, float]:
    if threshold < 1:
        raise ValueError("threshold must be positive")

    flat = image.flatten()

    counts = np.zeros(256, dtype=np.int64)
    colors = np.arange(256, dtype=np.int32).reshape(-1, 1)

    np.add.at(counts, flat, 1)

    valid_colors = counts > 0

    diffs = np.abs(colors - colors.T)
    mask = diffs < threshold

    groups = np.sum(mask * counts, axis=1)

    scores = groups * (image.size + 1) + counts

    scores[~valid_colors] = -1

    ans_ind = np.argmax(scores)

    ans = np.uint8(ans_ind)
    percent = float(groups[ans_ind] / image.size)

    return ans, percent
