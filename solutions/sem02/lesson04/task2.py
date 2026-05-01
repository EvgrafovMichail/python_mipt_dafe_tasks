import numpy as np


def get_dominant_color_info(
    image: np.ndarray,
    threshold: int = 5,
) -> tuple[np.uint8, float]:
    if threshold < 1:
        raise ValueError("threshold must be positive")

    counts = np.zeros(256, dtype=int)  # массив-счётчик, сколько раз какой пиксель попадётся
    for pixel in image.ravel():
        counts[pixel] += 1

    res_color = 0
    max_count = 0

    for i in range(256):
        if counts[i] == 0:
            continue

        left = max(0, i - threshold + 1)  # чтобы не выйти за границы
        right = min(255, i + threshold - 1)

        curr_sum = 0
        for j in range(left, right + 1):
            curr_sum += counts[j]

        if curr_sum > max_count:
            max_count = curr_sum
            res_color = i
        elif curr_sum == max_count:
            if counts[i] > counts[res_color]:
                res_color = i
    all_pixels = image.shape[0] * image.shape[1]
    percent = (max_count / all_pixels) * 100

    return np.uint8(res_color), float(percent)
