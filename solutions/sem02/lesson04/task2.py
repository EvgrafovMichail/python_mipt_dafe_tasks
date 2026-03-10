import numpy as np


def get_dominant_color_info(
    image: np.ndarray[np.uint8],
    threshold: int = 5,
) -> tuple[np.uint8, float]:
    if threshold < 1:
        # добавил сообщение об ошибки, т.к. иначе тест не проходит
        raise ValueError("threshold must be positive")

    hist = np.zeros(256, dtype=int)

    for i in image:
        for j in i:
            hist[int(j)] += 1

    all_pixels = image.shape[0] * image.shape[1]

    prefix = np.zeros(257, dtype=int)
    for i in range(256):
        prefix[i + 1] = prefix[i] + hist[i]

    res_color = 0
    res_count = 0

    for j in range(256):
        if hist[j] == 0:
            continue

        left = max(0, j - threshold + 1)
        right = min(255, j + threshold - 1)

        count = prefix[right + 1] - prefix[left]

        if count > res_count:
            res_count = count
            res_color = j

    percent = res_count / all_pixels * 100

    return np.uint8(res_color), percent
