import numpy as np


def get_dominant_color_info(
    image: np.ndarray,
    threshold: int = 5,
) -> tuple[np.uint8, float]:
    if threshold < 1:
        raise ValueError("threshold must be positive")

    arr = image.flatten()
    length = arr.size

    cnt = np.zeros(256, dtype=np.int64)
    for val in range(256):
        eq = arr == val
        cnt[val] = np.sum(eq)

    max_val = 0
    max_idx = 0
    for i in range(256):
        if cnt[i] == 0:
            continue

        left = max(0, i - threshold + 1)
        right = min(255, i + threshold - 1)

        cur = np.sum(cnt[left : right + 1])

        if cur > max_val:
            max_val = cur
            max_idx = i

    percent = (max_val / length) * 100
    return np.uint8(max_idx), percent
