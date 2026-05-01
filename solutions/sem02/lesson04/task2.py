import numpy as np


def get_dominant_color_info(
    image: np.ndarray,
    threshold: int = 5,
) -> tuple[np.uint8, float]:
    if threshold < 1:
        raise ValueError("threshold must be positive")

    histogram = np.zeros(256, dtype=int)

    flat_image = image.flatten()
    for pixel in flat_image:
        histogram[pixel] += 1

    max_sum = 0
    dominant_color = 0

    colors_with_pixels = np.where(histogram > 0)[0]

    for color in colors_with_pixels:
        left_bound = max(0, int(color) - threshold + 1)
        right_bound = min(255, int(color) + threshold - 1)
        current_sum = np.sum(histogram[left_bound : right_bound + 1])

        if current_sum > max_sum:
            max_sum = current_sum
            dominant_color = color

    percentage = (max_sum / image.size) * 100
    return np.uint8(dominant_color), float(percentage)


# Я знаю, что это долго но так и не придумал как можно еще больше векторизовать функцию
