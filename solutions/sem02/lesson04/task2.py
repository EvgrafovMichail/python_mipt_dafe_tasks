import numpy as np


def get_dominant_color_info(
    image: np.ndarray[np.uint8],
    threshold: int = 5,
) -> tuple[np.uint8, float]:
    # ваш код
    if threshold < 1:
        raise ValueError("threshold must be positive")

    pixels = image.flatten()

    value_counts = np.bincount(pixels, minlength=256).astype(np.int64)
    color_indices = np.arange(256, dtype=np.int32).reshape(-1, 1)

    is_present = value_counts > 0

    pairwise_diffs = np.abs(color_indices - color_indices.T)
    within_threshold = pairwise_diffs < threshold

    neighborhood_sums = np.sum(within_threshold * value_counts, axis=1)

    ranking_scores = neighborhood_sums * (image.size + 1) + value_counts
    ranking_scores[~is_present] = -1

    dominant_idx = np.argmax(ranking_scores)

    dominant_color = np.uint8(dominant_idx)
    percentage = float(neighborhood_sums[dominant_idx] / image.size)

    return dominant_color, percentage
