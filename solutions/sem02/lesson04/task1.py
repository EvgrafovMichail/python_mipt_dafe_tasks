import numpy as np


def pad_image(image: np.ndarray, pad_size: int) -> np.ndarray:
    if pad_size < 1:
        raise ValueError

    new_shape = tuple(s + 2 * pad_size for s in image.shape[:2]) + image.shape[2:]
    new_image = np.zeros(new_shape, dtype=image.dtype)
    new_image[pad_size:-pad_size, pad_size:-pad_size] = image
    return new_image


def blur_image(image: np.ndarray, kernel_size: int) -> np.ndarray:
    if kernel_size < 1 or kernel_size % 2 == 0:
        raise ValueError

    if kernel_size == 1:
        return image.copy()

    pad_size = kernel_size // 2
    padded_image = pad_image(image, pad_size)
    height, width = image.shape[:2]

    prefix_sum_table = np.zeros(
        (padded_image.shape[0] + 1, padded_image.shape[1] + 1) + image.shape[2:]
    )
    prefix_sum_table[1:, 1:] = padded_image.cumsum(axis=0).cumsum(axis=1)

    top_left = prefix_sum_table[0:height, 0:width]
    bottom_right = prefix_sum_table[
        kernel_size : kernel_size + height, kernel_size : kernel_size + width
    ]
    top_right = prefix_sum_table[0:height, kernel_size : kernel_size + width]
    bottom_left = prefix_sum_table[kernel_size : kernel_size + height, 0:width]

    window_sum = bottom_right + top_left - top_right - bottom_left
    blurred_image = (window_sum / (kernel_size * kernel_size)).astype(image.dtype)
    return blurred_image


if __name__ == "__main__":
    import os
    from pathlib import Path

    from utils.utils import compare_images, get_image

    current_directory = Path(__file__).resolve().parent
    image = get_image(os.path.join(current_directory, "images", "circle.jpg"))
    image_blured = blur_image(image, kernel_size=21)

    compare_images(image, image_blured)
