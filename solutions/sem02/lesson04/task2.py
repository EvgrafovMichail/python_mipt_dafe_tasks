import numpy as np


def get_dominant_color_info(
    image: np.ndarray[np.uint8],
    threshold: int = 5,
) -> tuple[np.uint8, float]:
    if threshold < 1:
        raise ValueError("threshold must be positive")

    pix_unique, count_pixs = np.unique(image, return_counts=True)

    count_all_pix = np.zeros(256)
    count_all_pix[pix_unique] = count_pixs

    sum_max = 0

    for mid in pix_unique:
        left = max(0, int(mid) - threshold + 1)
        r = min(255, int(mid) + threshold - 1)
        sum_curr = np.sum(count_all_pix[left : r + 1])

        if sum_curr > sum_max:
            moda = mid
            sum_max = sum_curr

    return moda, float(sum_max / image.size * 100)
