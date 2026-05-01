import numpy as np


def get_dominant_color_info(
    image: np.ndarray[np.uint8],
    threshold: int = 5,
) -> tuple[np.uint8, float]:
    if threshold < 1:
        raise ValueError("threshold must be positive")

    image = np.array(image, dtype=np.int64)

    u_values, u_counts = np.unique(image, return_counts=True)

    diff_matrix = u_values[..., np.newaxis] - u_values[np.newaxis, ...]

    mask_matrix = abs(diff_matrix) < threshold

    count_of_sml = np.sum(mask_matrix * u_counts, axis=1)

    best_i = np.argmax(count_of_sml)

    result_color = u_values[best_i]
    result_percent = (count_of_sml[best_i] / image.size) * 100

    return np.uint8(result_color), float(result_percent)
